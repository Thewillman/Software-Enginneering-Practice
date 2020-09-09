import jieba
import sys
from gensim import corpora, models, similarities

if __name__ == '__main__':
    fR = open(sys.argv[1],'r',encoding='UTF-8')
    base_data = fR.read()
    fR.close()

    # 1.将base_data中的数据按行分段并进行遍历后分词
    base_sentence = []
    s = ""
    cnt = 0
    sum = 0
    array = []
    for i in range(0,len(base_data)):
        if  '\u4e00' <= base_data[i] <= '\u9fff':
            s += base_data[i]
        elif base_data[i] == '，':
            #print(s)
            base_sentence.append(s)
            s = ""
    if s != "":
        #print(s)
        base_sentence.append(s)
        s = ""
    #print(base_sentence)
    base_items = [[i for i in jieba.lcut(item)] for item in base_sentence]
    #print(len(array))
    # 2.生成词典
    dictionary = corpora.Dictionary(base_items)
    # 3.通过doc2bow稀疏向量生成语料库
    corpus = [dictionary.doc2bow(item) for item in base_items]
    # 4.通过TF模型算法，计算出tf值
    tf = models.TfidfModel(corpus)
    # 5.通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    # 6.计算稀疏矩阵相似度，建立一个索引
    index = similarities.MatrixSimilarity(tf[corpus], num_features=num_features)

    # 7.处理测试数据
    fW = open(sys.argv[2], 'r', encoding='UTF-8')
    test_text = fW.read()
    fW.close()
    test_sentence = []
    s = ""
    cnt = 0
    sum = 0
    for i in range(0, len(test_text)):
        if '\u4e00' <= test_text[i] <= '\u9fff':
            s += test_text[i]
            cnt += 1
        elif test_text[i] == '，':
            #print(s)
            if s!="":
                test_sentence.append(s)
                array.append(cnt)
                sum += cnt
                cnt = 0
            s = ""
    if s != "":
        #print(s)
        test_sentence.append(s)
        array.append(cnt)
        sum += cnt
        cnt = 0
        s = ""
    print(test_sentence)
    for i in range(0,len(array)):
        array[i] = array[i]*1.0/sum
    test_items = [[i for i in jieba.cut(item)] for item in test_sentence]
    #print(len(test_items))
    ans = 0.0
    # 8.新的稀疏向量以及加权相似度
    array2 = []
    for i in range(0,len(test_items)):
        new_vec = dictionary.doc2bow(test_items[i])
        sim = index[tf[new_vec]]
        array2.append(sim[i])
        #ns += array[i]*sim[i]
    for i in range(0,len(array2)):
        ans += array2[i]*array[i]
    #print(ans)
    fR = open(sys.argv[3],'w',encoding='UTF-8')
    sim = str('%.15f'% ans)
    k = ""
    k+=sim[0]
    k+=sim[1]
    k+=sim[2]
    k+=sim[3]
    fR.write(k)
    fR.close()
    print(k)