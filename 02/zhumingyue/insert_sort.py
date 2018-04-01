# -*- coding:utf-8 -*-
# Author:Moon

l1 = [5,6,9,8,7,4]
for idx in range(1,len(l1)):
    tmp = l1[idx]
    tmp_idx = idx - 1
    while tmp_idx > -1:
        if l1[tmp_idx] > tmp:
            l1[tmp_idx+1] = l1[tmp_idx]
            tmp_idx -= 1
        else:
            break
    l1[tmp_idx+1] = tmp
print(l1)