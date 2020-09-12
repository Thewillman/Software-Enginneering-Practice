#orz加了些自己的数据
import jieba
import sys
import test
from gensim import corpora, models, similarities
import os
import time
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
if __name__ == '__main__':
    path = os.getcwd()
    #先测试作业给的样例
    path_homework = path + '\\sim_0.8'
    homework_files = os.listdir(path_homework)#获取当前目录下所有文件
    start = time.time()
    orig_position = path_homework + '\\' + 'orig.txt'
    orig_items = orig_solve(orig_position)
    end = time.time()
    print('处理成功orig.txt,耗时%f，开始进行文件比对'%(end - start))
    #接下来对各个样例数据进行比对

    #加式修改文本orig_0.8_add.txt
    start = time.time()
    orig_add_position = path_homework + '\\' + 'orig_0.8_add.txt'
    orig_sim_add_items,array = text_solve(orig_add_position)
    ans = test.cal_similarity(orig_items,orig_sim_add_items,array)
    end = time.time()
    print('orig_0.8_add.txt查重率为：%.2f,耗时为%f' %(ans,(end - start)))

    # 删式修改文本orig_0.8_del.txt
    start = time.time()
    orig_del_position = path_homework + '\\' + 'orig_0.8_del.txt'
    orig_sim_del_items, array = text_solve(orig_del_position)
    ans = test.cal_similarity(orig_items,orig_sim_del_items,array)
    end = time.time()
    print('orig_0.8_del.txt查重率为：%.2f,耗时为%f' % (ans, (end - start)))

    # 乱序文本1 orig_0.8_dis_1.txt
    start = time.time()
    orig_dis_1_position = path_homework + '\\' + 'orig_0.8_dis_1.txt'
    orig_sim_dis_1_items, array = text_solve(orig_dis_1_position)
    ans = test.cal_similarity(orig_items,orig_sim_dis_1_items,array)
    end = time.time()
    print('orig_0.8_dis_1.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    # 乱序文本2 orig_0.8_dis_3.txt
    start = time.time()
    orig_dis_3_position = path_homework + '\\' + 'orig_0.8_dis_3.txt'
    orig_sim_dis_3_items, array = text_solve(orig_dis_3_position)
    ans = test.cal_similarity(orig_items, orig_sim_dis_3_items,array)
    end = time.time()
    print('orig_0.8_dis_3.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    # 乱序文本3 orig_0.8_dis_7.txt
    start = time.time()
    orig_dis_7_position = path_homework + '\\' + 'orig_0.8_dis_7.txt'
    orig_sim_dis_7_items, array = text_solve(orig_dis_7_position)
    ans = test.cal_similarity(orig_items, orig_sim_dis_7_items,array)
    end = time.time()
    print('orig_0.8_dis_7.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    # 乱序文本4 orig_0.8_dis_10.txt
    start = time.time()
    orig_dis_10_position = path_homework + '\\' + 'orig_0.8_dis_10.txt'
    orig_sim_dis_10_items, array = text_solve(orig_dis_10_position)
    ans = test.cal_similarity(orig_items, orig_sim_dis_10_items,array)
    end = time.time()
    print('orig_0.8_dis_10.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    # 乱序文本5 orig_0.8_dis_15.txt
    start = time.time()
    orig_dis_15_position = path_homework + '\\' + 'orig_0.8_dis_15.txt'
    orig_sim_dis_15_items, array = text_solve(orig_dis_15_position)
    ans = test.cal_similarity(orig_items, orig_sim_dis_15_items,array)
    end = time.time()
    print('orig_0.8_dis_15.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    # mix文本 orig_0.8_mix.txt
    start = time.time()
    orig_mix_position = path_homework + '\\' + 'orig_0.8_mix.txt'
    orig_sim_mix_items, array = text_solve(orig_mix_position)
    ans = test.cal_similarity(orig_items, orig_sim_mix_items,array)
    end = time.time()
    print('orig_0.8_mix.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    # rep文本 orig_0.8_rep.txt
    start = time.time()
    orig_rep_position = path_homework + '\\' + 'orig_0.8_rep.txt'
    orig_sim_rep_items, array = text_solve(orig_rep_position)
    ans = test.cal_similarity(orig_items, orig_sim_rep_items,array)
    end = time.time()
    print('orig_0.8_rep.txt查重率为：%.2f,耗时为%f' % (ans,(end - start)))

    print('<-------------接下来是我自写的数据集------------------>')

