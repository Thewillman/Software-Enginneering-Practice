import random
def add(test_text):#增字，目前只支持每隔固定距离添加固定长度随机汉字
    a,b = eval(input("请输入划分段的字数以及要添加随机汉字的长度，用逗号隔开:"))
    s = ""
    cnt = 0
    for i in range(0,len(test_text)):
        s += test_text[i]
        cnt += 1
        if cnt == a:
            cnt = 0
            for j in range(0,b):
                s+=chr(random.randint(0x4e00, 0x9fbf))
    return s

def delete(test_text):#删字，目前只支持每隔固定距离删除固定长度随机汉字
    a, b = eval(input("请输入划分段的字数以及要删除随机汉字的长度，用逗号隔开:"))
    s = ""
    cnt = 0
    for i in range(0, len(test_text)):
        if cnt == a:
            cnt = 0
            for j in range(0, b):
                i += 1
                if i == len(test_text):
                    break
        if i == len(test_text):
            break
        s += test_text[i]
        cnt += 1
    return s

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def chaos_sort(str1):
    str1_len = len(str1)
    list1 = list(str1)
    for i in range(0,str1_len):
        k = random.randint(0, str1_len-i-1)
        #print(list1[k],list1[str1_len-i-1])
        list1[k],list1[str1_len-i-1] = swap(list1[k],list1[str1_len-i-1])
        #print(list1[k], list1[str1_len-i-1])
    str1 = ""
    for i in range(0, str1_len):
        str1+=list1[i]
    #print(str1)
    return str1

def dis(test_text):#乱序，目前只支持逗号分割，句号分割以及每隔一段距离n次乱序的操作
    a,b = eval(input("请输入划分模式（1表示逗号分割，2表示句号分割，3表示自己定分段字数）以及每次乱序的次数:"))
    s = ""
    temp = ""
    if a == 1 or a == 2:
        if a == 1:
            str1 = '，'
        elif a == 2:
            str1 = '。'
        for i in range(0, len(test_text)):
            temp += test_text[i]
            if test_text[i] == str1:
                for j in range(0,b):
                    temp = chaos_sort(temp)
                #print(temp)
                s += temp
                temp = ""
        if temp != "" :
            for j in range(0, b):
                chaos_sort(temp)
            s += temp
            temp = ""
    else:
        c = eval(input("请输入分段长度："))
        cnt = 0
        for i in range(0, len(test_text)):
            temp += test_text[i]
            cnt += 1
            if cnt == c:
                for j in range(0,b):
                    chaos_sort(temp)
                print(temp)
                s += temp
                cnt = 0
                temp = ""
        if temp != "" :
            for j in range(0, b):
                chaos_sort(temp)
            s += temp
            temp = ""
    return s
def mix(test_text):#增删结合
    str1 = add(test_text)
    str1 = delete(str1)
    return str1
def rep(test_text):#增删乱序结合
    str1 = add(test_text)
    print(str1)
    str1 = delete(str1)
    print(str1)
    str1 = dis(str1)
    return str1
if __name__ == '__main__':
    test = open("My_database1\\orig.txt",'r',encoding = 'UTF-8')
    test_text = test.read()
    test.close()
    str1 = input("请输入创造相似文本的模式(add,del,dis,mix,rep):")
    str1.upper()
    if str1 == "ADD":
        change_text = add(test_text)
    elif str1 == "DEL":
        change_text = delete(test_text)
    elif str1 == "DIS":
        change_text = dis(test_text)
    elif str1 =="MIX":
        change_text = mix(test_text)
    else:
        change_text = rep(test_text)
    #print(change_text)
    change = open("My_database1\\orig_rep.txt",'w',encoding = 'UTF-8')
    change.write(change_text)
    change.close()
    print("已按%s模式生成相应文本:D",str1)
    print(0)
