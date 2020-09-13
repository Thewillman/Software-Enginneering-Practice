#orz加了些自己的数据
import jieba
import sys
import test#引用一下计算程序，不然代码属实太长
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
def write_dir(ans,ans_position):
    str1 = str('0.2f' %ans)
    ans_text = open(ans_position,'w',encoding='UTF-8')
    ans_text.write(str1)
    ans_text.close()
    #print('0')
def solve(orig_position,text_position,ans_position):
    orig_items = orig_solve(orig_position)
    text_items,array = text_solve(text_position)
    ans = test.cal_similarity(orig_items,text_items,array)
    write_dir(ans,ans_position)
    print('orz查重结果为%.2f' %ans)

