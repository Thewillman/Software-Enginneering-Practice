#orz加了些自己的数据
import jieba
import sys
import test#引用一下计算程序，不然代码属实太长
from gensim import corpora, models, similarities
import os
import time

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

def orig_solve(orig_position):
    orig = open(orig_position, 'r', encoding='UTF-8')
    orig_text = orig.read()
    orig.close()
    # 1.将原始文本分句并每句用jieba_lcut分词
    orig_items = test.create_jieba_list(orig_text)
    return orig_items

def text_solve(text_position):
    text = open(text_position, 'r', encoding='UTF-8')
    test_text = text.read()
    text.close()
    # 1.将原始文本分句并每句用jieba_lcut分词
    text_items = test.create_jieba_list(test_text)
    array = test.cal_sentence_weight(test_text)
    return text_items,array

def write_dir(ans,ans_position):
    str1 = str('0.2f' %ans)
    ans_text = open(ans_position,'w',encoding='UTF-8')
    ans_text.write(str1)
    ans_text.close()
    #print('0')

def solve_tfidf(orig_position,text_position,ans_position):
    orig_items = orig_solve(orig_position)
    text_items,array = text_solve(text_position)
    ans = test.cal_similarity_tfidf(orig_items,text_items,array)
    write_dir(ans,ans_position)
    print('orzTF-IDF模型查重结果为%.2f' %ans)

def solve_lda(orig_position,text_position,ans_position):
    orig_items = orig_solve(orig_position)
    text_items,array = text_solve(text_position)
    ans = cal_similarity_lda(orig_items,text_items,array)
    write_dir(ans,ans_position)
    print('orzLDA模型查重结果为%.2f' %ans)

def solve_lsi(orig_position,text_position,ans_position):
    orig_items = orig_solve(orig_position)
    text_items,array = text_solve(text_position)
    ans = cal_similarity_lsi(orig_items,text_items,array)
    write_dir(ans,ans_position)
    print('orzLSI模型查重结果为%.2f' %ans)
