#列表

nums = [1,2,3,4,5,6]
users = ['woniu','wd','kk']

#索引
nums[0]

#遍历列表
for i in nums:
	print(i)

for i in range(len(nums)):
	print(nums[i])

#获取list元素的数量
len(nums)

#获取list中元素最大值、最小值
max(nums) min(nums)

#判断元素是否在list中存储
 1 in nums    True False

#删除列表中元素
del nums[0]

#切片
list[start:end:step]
list[::step]
list[start:end]
list[:end]
list[start:]
list[:]

#常用函数
append 添加元素到list最右侧
clear 清空list中的元素
copy 复制list中的所有元素到新list中并返回
count 计算list中存在相同元素的数量
extend 将一个可遍历数据中的所有元素追加到list后
index 获取元素在list中的位置
insert 在list指定位置添加元素
pop 弹出list中指定位置的元素（默认最右侧）
remove 移除list中指定的元素
reverse对list中元素进行反转
sort 对list中元素进行排序

#查看数据类型可使用的函数
dir(nums)

#查看函数使用方法
help(nums.append)

#队列
先进先出
list.append + list.pop(0)
#堆栈
先进后出
list.append + list.pop


元组基本上与列表相同操作，元组不可改变。


