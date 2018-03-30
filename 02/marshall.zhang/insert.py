#coding=utf-8
list_num = [1,4,3,2434,6,222,45,8,12,333,777,234,21,34,23,25,43,38,33,70,9,17,28]
num_index = 1

while num_index < len(list_num):
    item = list_num.pop(num_index) #从第二个元素开始Pop出下一个元素准备做插入
    i = 0
    while i < num_index:     #对pop出的那个元素之前的虚拟列表做遍历
        if item > list_num[i]:
            list_num[i:i] = [item] #将pop出的元素插入到对应的位置
            break
        i+=1
    num_index+=1
print(list_num)


