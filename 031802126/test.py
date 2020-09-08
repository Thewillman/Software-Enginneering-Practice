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
    cntl = 0
    for i in range(0,len(base_data)):
        if base_data[i] == ' ':
            continue
        elif base_data[i] == '”':
            cntl += 1
        elif base_data[i] == '\n':
            if i == 0 or base_data[i-1] == '\n' or base_data[i-1] == '“' or base_data[i-1] == "：" or base_data[i-1] == ' ' or base_data[i-1] == '。' or base_data[i-1] == '——':
                continue
            else:
                base_sentence.append(s)
                print(s)
                array.append(cnt)
                sum += cnt
                s = ""
                cnt = 0
                continue
        elif base_data[i] == '。' or base_data[i] == '？' or base_data[i] == '！' or base_data[i] == '……':
            #print(s)
            if cntl == 0:
                base_sentence.append(s)
                print(s)
                array.append(cnt)
                sum += cnt
                s = ""
                cnt = 0
                continue
        elif base_data[i] == '“':
            base_sentence.append(s)
            print(s)
            array.append(cnt)
            sum += cnt
            s = ""
            cnt = 0
            continue
        else:
            s += base_data[i]
            cnt += 1
    if cnt:
        base_sentence.append(s)
        array.append(cnt)
        sum += cnt
    cnt = 0
    base_items = [[i for i in jieba.lcut(item)] for item in base_sentence]
    base_items.append([""])
    for i in range(0,len(array)):
        array[i] = float(array[i]/sum)
    #print(array)
    #print(base_items)
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
    cntl = 0
    for i in range(0, len(test_text)):
        if test_text[i] == ' ':
            continue
        elif test_text[i] == '“':
            cntl +=1
        elif test_text[i] == '\n':
            if i == 0 or test_text[i - 1] == '\n' or test_text[i - 1] == '“' or test_text[i - 1] == "：" or test_text[i-1] == '——' or test_text[i-1] == ' ' or test_text[i-1] == '。':
                continue
            else:
                test_sentence.append(s)
                #print(s)
                s = ""
                continue
        elif test_text[i] == '。' or test_text[i] == '？' or test_text[i] == '！' or test_text[i] == '……' :
            if cntl == 0:
                test_sentence.append(s)
                #print(s)
                s = ""
                continue
        elif test_text[i] == '“':
            cntl -= 1
            test_sentence.append(s)
            #print(s)
            s = ""
            continue
        else:
            s += test_text[i]
    if s != "":
        test_sentence.append(s)
    test_items = [[i for i in jieba.cut(item)] for item in test_sentence]
    #print(test_words)

    # 8.新的稀疏向量以及加权相似度
    ans = 0.0
    for i in range(0,len(test_items)):
        new_vec = dictionary.doc2bow(test_items[i])
        sim = index[tf[new_vec]]
        ans += sim[i]*array[i]
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