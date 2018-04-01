# -*- coding:utf-8 -*-
# Author:Moon
l1 = [3, 6, 9, 11, 18, 5, 6, 1]
l1.sort()
start = 0
end = len(l1) - 1
is_find = False
try:
    find = int(input("请输入要查找的数字:"))
except ValueError as e:
    print("输入错误，请输入数字")

while start <= end:
    middle = (start+end)//2

    if l1[middle] == find:
        is_find = True
        break
    elif l1[middle] > find:
        end = middle -1
    elif l1[middle] < find:
        start = middle+1
if is_find:
    print("找到了")
else:
    print("没找到")