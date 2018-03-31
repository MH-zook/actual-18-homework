#网上参考的例子

array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

def sort(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            temp = array[i]    
            index = i          
            while index > 0 and array[index - 1] > temp:
                array[index] = array[index - 1]
                index -= 1
            array[index] = temp 
    print(array)

sort(array)

'''
插入排序总结：

当前需要排序的元素(array[i])，跟已经排序好的最后一个元素比较(array[i-1])，如果满足条件继续执行后面的程序，否则循环到下一个要排序的元素。
缓存当前要排序的元素的值，以便找到正确的位置进行插入。
排序的元素跟已经排序号的元素比较，比它大的向后移动(升序)。
要排序的元素，插入到正确的位置。
'''



