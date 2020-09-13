import jieba
import sys
from gensim import corpora, models, similarities
from jieba import analyse
import time
import logging


class TextSameError(Exception):  # 文本不同相似度却100%

    def __init__(self):
        print("文本不一样为什么会完全一样捏？")

    def __str__(self, *args, **kwargs):
        return "再检查一下代码哦"


class TextDifferentError(Exception):  # 文本一致相似度不是100%

    def __init__(self):
        print("自己和自己比，怎么会不一样呢？")

    def __str__(self, *args, **kwargs):
        return "再检查一下代码哦"


class NoChineseError(Exception):  # 比对文本压根没有汉字，相似度直接判0


    def __init__(self):
        print("汉字都没有比对🔨呢")
        ans_txt = open(sys.argv[3], 'w', encoding='UTF-8')
        sim = str(0.00)
        ans_txt.write(sim)
        ans_txt.close()
        print("0")

    def __str__(self, *args, **kwargs):
        return "找篇有汉字的来吧"

#@profile
def create_jieba_list(test_data):  # 将文本分句并且每个句子进行分词
    test_sentence = []
    s = ""
    for i in range(0, len(test_data)):
        if '\u4e00' <= test_data[i] <= '\u9fff':  # 只记录汉字
            s += test_data[i]
        elif test_data[i] == '。':  # 以句号作为分句标准
            # print(s)
            if s != "":  # 防止出现一连串符号
                test_sentence.append(s)
                s = ""
    if s != "":  # 可能还有文本需要加上
        # print(s)
        test_sentence.append(s)
        s = ""
    test_items = [[i for i in jieba.lcut(item)] for item in test_sentence]
    return test_items

#@profile
def cal_sentence_weight(test_data):  # array数组存抄袭文本每句占总文本汉字的权重，cnt是每个句子汉字长度，sum是总文本汉字长度
    array = []
    cnt = 0
    sum = 0
    # 统计句子汉字长度以及总文本汉字长度
    for i in range(0, len(test_data)):
        if '\u4e00' <= test_data[i] <= '\u9fff':
            cnt += 1
        elif test_data[i] == '。':
            if cnt:
                array.append(cnt)
                sum += cnt
                cnt = 0
    if cnt != 0:
        # print(s)
        array.append(cnt)
        cnt = 0
    # 计算权重
    if sum == 0:
        raise NoChineseError
    else:
        for i in range(0, len(array)):
            array[i] = array[i] * 1.0 / sum
        return array

#@profile
def cal_similarity_tfidf(orig_items, orig_sim_items, array):
    # 对原始文本用gensim库中的doc2bow和corpora进行处理，采用tfidf模型
    # 生成词典
    dictionary = corpora.Dictionary(orig_items)
    # 通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(item) for item in orig_items]
    # 通过TF模型算法，计算出tf值
    tf = models.TfidfModel(corpus)
    # 通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    # 计算稀疏矩阵相似度，建立一个索引
    index = similarities.MatrixSimilarity(tf[corpus], num_features=num_features)

    # 开始对抄袭文本的相似度进行计算
    ans = 0.0
    for i in range(0, len(orig_sim_items)):
        # 把每个分好词的句子建立成新的稀疏向量并代入模型计算相似度
        orig_sim_vec = dictionary.doc2bow(orig_sim_items[i])
        sim = index[tf[orig_sim_vec]]
        sim_max = max(sim)
        if sim_max < 0.0025:  # 对于相似度低于0.25%的句子我们直接视为不相关
            continue
        try:
            ans += max(sim) * array[i]  # 显然我们这里要取最高相似度而不是一一对应，可能会有下标超界的错误
        except IndexError:
            print("orz下标超界了")
        else:
            continue
    return ans

def cal_similarity_lsi(orig_items, orig_sim_items, array):
    # 对原始文本用gensim库中的doc2bow和corpora进行处理，采用tfidf模型
    # 生成词典
    dictionary = corpora.Dictionary(orig_items)
    # 通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(item) for item in orig_items]
    # 通过TF模型算法，计算出tf值
    lsi = models.LsiModel(corpus)
    # 通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    # 计算稀疏矩阵相似度，建立一个索引
    index = similarities.MatrixSimilarity(lsi[corpus], num_features=num_features)

    # 开始对抄袭文本的相似度进行计算
    ans = 0.0
    for i in range(0, len(orig_sim_items)):
        # 把每个分好词的句子建立成新的稀疏向量并代入模型计算相似度
        orig_sim_vec = dictionary.doc2bow(orig_sim_items[i])
        sim = index[lsi[orig_sim_vec]]
        sim_max = max(sim)
        if sim_max < 0.0025:  # 对于相似度低于0.25%的句子我们直接视为不相关
            continue
        try:
            ans += max(sim) * array[i]  # 显然我们这里要取最高相似度而不是一一对应，可能会有下标超界的错误
        except IndexError:
            print("orz下标超界了")
        else:
            continue
    return ans

def cal_similarity_lda(orig_items, orig_sim_items, array):
    # 对原始文本用gensim库中的doc2bow和corpora进行处理，采用tfidf模型
    # 生成词典
    dictionary = corpora.Dictionary(orig_items)
    # 通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(item) for item in orig_items]
    # 通过TF模型算法，计算出tf值
    lda = models.LdaModel(corpus)
    # 通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    # 计算稀疏矩阵相似度，建立一个索引
    index = similarities.MatrixSimilarity(lda[corpus], num_features=num_features)

    # 开始对抄袭文本的相似度进行计算
    ans = 0.0
    for i in range(0, len(orig_sim_items)):
        # 把每个分好词的句子建立成新的稀疏向量并代入模型计算相似度
        orig_sim_vec = dictionary.doc2bow(orig_sim_items[i])
        sim = index[lda[orig_sim_vec]]
        sim_max = max(sim)
        if sim_max < 0.0025:  # 对于相似度低于0.25%的句子我们直接视为不相关
            continue
        try:
            ans += max(sim) * array[i]  # 显然我们这里要取最高相似度而不是一一对应，可能会有下标超界的错误
        except IndexError:
            print("orz下标超界了")
        else:
            continue
    return ans

def cal_similarity_word2vec(orig_items, orig_sim_items, array):
    # 对原始文本用gensim库中的doc2bow和corpora进行处理，采用tfidf模型
    # 生成词典
    dictionary = corpora.Dictionary(orig_items)
    # 通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(item) for item in orig_items]
    # 通过TF模型算法，计算出tf值
    word2vector = models.word2vec(corpus)
    # 通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    # 计算稀疏矩阵相似度，建立一个索引
    index = similarities.MatrixSimilarity(word2vector[corpus], num_features=num_features)

    # 开始对抄袭文本的相似度进行计算
    ans = 0.0
    for i in range(0, len(orig_sim_items)):
        # 把每个分好词的句子建立成新的稀疏向量并代入模型计算相似度
        orig_sim_vec = dictionary.doc2bow(orig_sim_items[i])
        sim = index[word2vector[orig_sim_vec]]
        sim_max = max(sim)
        if sim_max < 0.0025:  # 对于相似度低于0.25%的句子我们直接视为不相关
            continue
        try:
            ans += max(sim) * array[i]  # 显然我们这里要取最高相似度而不是一一对应，可能会有下标超界的错误
        except IndexError:
            print("orz下标超界了")
        else:
            continue
    return ans
if __name__ == '__main__':
    start = time.time()
    orig = open(sys.argv[1], 'r', encoding='UTF-8')
    orig_text = orig.read()
    orig.close()
    # 载入停用词
    jieba.analyse.set_stop_words("stopword.txt")
    # 1.将原始文本分句并每句用jieba_lcut分词
    orig_items = create_jieba_list(orig_text)

    # print(len(array))

    # 7.对待评测文本进行同样处理
    orig_sim = open(sys.argv[2], 'r', encoding='UTF-8')
    orig_sim_text = orig_sim.read()
    orig_sim.close()
    orig_sim_items = create_jieba_list(orig_sim_text)
    # print(test_sentence)

    array = cal_sentence_weight(orig_sim_text)
    # print(len(test_items))
    ans = cal_similarity_tfidf(orig_items, orig_sim_items, array)
    print('tf-idf模型相似度: %.2f' %ans)
    ans = cal_similarity_lsi(orig_items, orig_sim_items, array)
    print('lsi模型相似度:%.2f' %ans)
    ans = cal_similarity_lda(orig_items, orig_sim_items, array)
    print('lda模型相似度:%.2f' % ans)
    ans = cal_similarity_hdp(orig_items, orig_sim_items, array)
    print('hdp模型相似度:%.2f' % ans)
    ans = cal_similarity_word2vec(orig_items, orig_sim_items, array)
    print('word2vec模型相似度:%.2f' % ans)
    ans = cal_similarity_tfidf(orig_items, orig_sim_items, array)
    if abs(ans - 1.00) <= 0.000001 :
        raise TextSameError
    else:
        ans_txt = open(sys.argv[3], 'w', encoding='UTF-8')
        sim = str('%.2f' % ans)
        ans_txt.write(sim)
        ans_txt.close()
        end = time.time()
    print(0)
