# encoding: utf-8
"""
作业2：二分查找算法

"""

a = [5, 13, 19, 21, 37, 56, 64, 75, 80, 88, 92, 100]


def binary_search(li, find):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        # 判断中位 ，低位，高位 是否等于查找数值，可以减少循环次数
        if li[mid] == find:
            return mid
        elif li[low] == find:
            return low
        elif li[high] == find:
            return high
        elif li[mid] > find:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search(a, -20))
for i in a:
    print(binary_search(a, i))
print(binary_search(a, 101))
