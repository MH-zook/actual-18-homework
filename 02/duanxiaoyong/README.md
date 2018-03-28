# pyton 序列

### 列表是什么
* 有序的
* 可遍历的
* 可追加/可插入
* 可删除/可弹出
* 可修改
* 长度不定【修改、删除、添加，如果不做动作，长度固定】
### 列表的定义
* 定义
```python
   - num = [1,2,3,4,5,6,7,8]
   - dxy = ['a','b','c','d','e']
```
* 使用中括号包含
* 每个元素之间使用逗号分隔
* 可包含任意数据类型
  - 布尔值类型
  - 数值类型
  - 字符串类型
  - 可以嵌套列表类型
### 访问与修改列表
- 列表是有序的数据集，通过列表名[索引]的方式访问列表中的元素
```python
    >>> num = [1,2,3,4,5,6,7,8]
  >>> num[0]
1
>>> num[4]
5
>>> num[-1]
8
>>>
```
- 索引编号
    - 从左向右依次为0，1，2，3，…，n – 1
    - 从右向左一次为-1，-2，-3，…，-n
- 访问元素的索引必须存在，否则报错
- 元素修改
```python
>>> num[0]=100
>>> num
[100, 2, 3, 4, 5, 6, 7, 8]
>>> num[5]=1000
>>> num
[100, 2, 3, 4, 5, 1000, 7, 8]
>>>
```
- 通过直接给 列表名[索引] 修改对应索引位置的值
```python
>>> num
[100, 2, 3, 4, 5, 1000, 7, 8]
>>> num[-1]
8
>>> num[-2]
7
>>> num[-3]
1000
>>>
```
- 修改元素的索引必须存在，否则报错
```python
>>> num[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```
- bool转化，非空为True、空为Flase
```python
>>> bool([1,2])
True
>>> bool([])
False
>>>
```
### 遍历列表
- 使用for访问列表中所有的元素
```python
num = [1,2,3,4,5,6,7,8]

for i in num:
    print(i)
```
- 类型转换
- 可以通过函数list将其他可遍历的类型转化为列表
- 使用range函数快速创建序列
```python
for i in range(1,4):
    print(i)
```
- range(end) 创建从0到end-1的连续整数组成的序列
- range(start, end) 创建从start到end-1的连续整数组成的序列
- range(start, end, step)创建从start到end-1的每间隔stop个整数组成的序列

###### 定义一个最大值与list比较大小
 - 伪代码思路
    - 假设第一个最大: (1)
    - 第二次比较: 8 > (1)5 => (2)
    - 第三次比较: 7 > (2)8 => (2)
    - 第四次比较: 10 > (2)8 => (4)
    - 第五次比较: 20 > (4)10 => (5)
    - 第六次比较:  2 > (5)20 => (5)
    - 第七次比较:  6 > (5)20 => (5)
    - 第八次比较:  9 > (5)20 => (5)

```python
nums = [5, 8, 7, 10, 20, 2, 6, 9]
nums = [(1, 'kk'), (2, 'kk')]

max_index = 0
idx = 0
for num in nums:
    if num > nums[max_index]:
        max_index = idx
    idx += 1
```
###### 索引取最大值练习
 - 伪代码思路
    - 假设第一个最大: 5(1)
    - 第二次比较: 8(2) > 5(1) => 8(2)
    - 第三次比较: 7(3) > 8(2) => 8(2)
    - 第四次比较: 10(4) > 8(2) => 10(4)
    - 第五次比较: 20(5) > 10(4) => 20(5)
    - 第六次比较:  2(6) > 20(5) => 20(5)
    - 第七次比较:  6(7) > 20(5) => 20(5)
    - 第八次比较:  9(8) > 20(5) => 20(5)
```python
#索引取做大值
nums = [5, 8, 7, 10, 20, 2, 6, 9]
#定义一个索引
max_index1 = 0
idx1 = 0
for num in nums:
    if num >nums[max_index1]:
        max_index =idx
    idx +=1
```
#### 交互模式字符串转换list
```python
print(list('abcd')) #pychrm交互式
>>> list('dxy,abc') #python3 执行
['d', 'x', 'y', ',', 'a', 'b', 'c']
>>>
```
### 列表常见操作
- len
```python
>>> num
[100, 2, 3, 4, 5, 1000, 7, 8]
>>> len(num)
8

```
- max
```python
>>> max(num)
1000

```
- del
```python
>>> del(num[1])
>>> num
[100, 3, 4, 5, 1000, 7, 8]

```
### 列表运算
- 加(+)
    - 必须为两个list相加
```python
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
```

- 乘(*)
    - 必须一个为整数
```python
>>> [1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>
```
### 切片
* 按照规则获取list中一部分元素生成新的list
    - list[start:end:step]

    - list[::step]
    - list[start:end]
    - list[:end]
    - list[start:]
    - list[:]
#### 切片的应用
* 复制数组
    * 引用、复制
    ```python
    >>> num=list(range(10))
    >>> num
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> nums_1 =num
    >>> nums_1[1]=20
    >>> num
    [0, 20, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> id(num)
    140243791733960 用id(num)表示内存地址

    ```
* 反转list
```python
>>> num[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 20, 0]
```
* 获取索引为偶数的元素组成的list
```python
>>> num[::2]
[0, 2, 4, 6, 8]
```
* 获取索引为奇数的元素组成的list
```python
>>> num[1::2]
[20, 3, 5, 7, 9]
>>>
```
#### 练习

* 找出 nums=[6, 11, 7, 9, 4, 2, 1]中最大的数字
- 移动nums中最大的数字到最后
- 提示:伪代码
- 从右到左依次两两比较，如果前面比后面大，则交换位置
- 第1次: 6，11比较，前面小，不交换[6, 11, 7, 9, 4, 2, 1]
- 第2次: 11, 7比较，前面大，交换[6, 7, 11, 9, 4, 2, 1]
- 第3次: 11, 9比较，前面大，交换[6, 7, 9, 11, 4, 2, 1]
- 第4次: 11, 4比较，前面大，交换[6, 7, 9, 4, 11, 2, 1]
- 第5次: 11, 2比较，前面大，交换[6, 7, 9, 4, 2, 11, 1]
- 第6次: 11, 1比较，前面大，交换[6, 7, 9, 4, 2, 1, 11]
- 交换元素
- tmp = a; a=b; b = tmp;
    - a, b = b, a''
脚本如下：😁【冒泡】
```python
nums=[6, 11, 7, 9, 4, 2, 1]
#nums[0] num[1]
#nums[1] num[2]
#nums[3] num[4]
#i, i+1 => 0->n-2

n = len(nums)
for i in range(n-1):
    if nums[i] > nums[i+1]:
        temp = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = temp

print(nums)
```
### 列表中的函数
- append 添加元素到list最右侧,append放的是一个整体
```python
>>> num.append([1,2,3])
>>> num
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 'a', 'b', 'c', [1, 2, 3]]
>>>
```
- clear 清空list中的元素
```python
>>> nums
[1, 2, 3, 4, 5]
>>> nums.clear()
>>> num
[]
```
- copy 复制list中的所有元素到新list中并返回
```python
>>> num = list(range(1,10))
>>> num
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> num1 =num.copy()
>>> num1
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
- count 计算list中存在相同元素的数量
```python
>>> nums
[1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6]
>>> nums.count(6)
6
>>>
```
- extend 将一个可遍历数据中的所有元素追加到list后，是把每一个元素分解追加
```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
>>> num.extend('abc')
>>> num
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 'a', 'b', 'c']
```
- index 获取元素在list中的位置
```python
>>> nums
[1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6]
>>> nums.index(3)
4
>>> nums.index(6)
7  存在多个  默认第一个返回值
>>>

元素不存在则报错！
```
- insert 在list指定位置添加元素
- pop 弹出list中指定位置的元素（默认最右侧）
```python
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nums.pop(2)
3
>>> nums.pop(0)
1
```
- remove 移除list中指定的元素
```python
>>> nums.remove(6)
>>> nums
[2, 4, 5, 7, 8, 9]
```
- reverse对list中元素进行反转
```python
>>> nums.reverse()
>>> nums
[9, 8, 7, 5, 4, 2]
```
- sort 对list中元素进行排序
```python
[9, 8, 7, 5, 4, 2]
>>> nums.sort()
>>> nums
[2, 4, 5, 7, 8, 9]
```
- len 显示列表的长度
- max 显示列表的最大值
- min 显示列表的最小值
- sum 显示所有元素的和
```python
nums = [1,3,5,7]
print(sum(nums))
```
- range函数快速创建序列
     - range(end) 创建从0到end-1的连续整数组成的序列range(0,end,1)
     - range(start, end) 创建从start到end-1的连续整数组成的序列--range(start,end,1)
     - range(start, end, step)创建从start到end-1的每间隔stop个整数组成的序列
        - 类似：range（start，start+step，start+2step,start+nstep <end）range(1,10,2)

```python
>>> list(range(0,20,3)) #闭左不闭右，每3个生成一个右边
[0, 3, 6, 9, 12, 15, 18]
倒序：
>>> list(range(9,0,-1))
[9, 8, 7, 6, 5, 4, 3, 2, 1]

```
练习：list的总和,count总数
```python
nums = [1,3,5,7]
totle = 0
count =0
ji = 1
for i in nums:
    totle +=i
    count +=1
    ji *=i
print(totle,count,ji)

```
练习1：
- Todolist
- 提示用户输入do或者任务(非do)
- 如果用户输入任务，则添加到list中
- 如果用户输入do，当任务为空时则打印无任务并退出，否则从list中根据先进先出原则打印任务
```python
jobs = []

while True:
    prompt = input('请输入任务名称/do:')
    if prompt == 'do':
        if jobs: #if len(jobs) > 0
            print('请完成任务:' + jobs.pop(0))
        else:
            print('所有任务已完成，可以放心下班啦')
            break
    else:
        jobs.append(prompt)
 ```
练习2
- 获取两个list中相同的元素到第三个列表中
- nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
- nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]
- 保证第二个练习中第三个列表中元素不重复

```python
nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]
num_3 = []

for i in nums_1:
    if i in nums_2 and i not in num_3:
        num_3.append(i)
print(num_3)
```

### 元组
- 不可变的列表
- 定义
- 使用小括号包含
- 每个元素之间使用逗号分隔
- 可包含任意数据类型
- 如果元组只有一个元素时，元素后的逗号不能省略

##### 访问与修改元组
- 元组是有序的数据集，通过元组名[索引]的方式访问元组中的元素
- 索引编号
- 从左向右依次为0，1，2，3，…，n – 1
- 从右向左一次为-1，-2，-3，…，-n
- 访问元素的索引必须存在，否则报错
- 元素不能修改
- 使用for访问元组中所有的元素

##### 元组的四则运算
- 加(+)
    - 必须为两个tuple相加
- 乘(*)
    - 必须一个为整数
```python
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> (1,2,3)*2
(1, 2, 3, 1, 2, 3)
>>>
```
##### 类型转换
- 可以通过函数tuple将其他可遍历的类型转化为元组
字符串转化元组：
```
>>> tuple('qwert')
('q', 'w', 'e', 'r', 't')
```
数值序列转化元组
```python
>>> tuple(range(10))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```
元组转化布尔
```python
>>> bool((1,))
True
>>> bool(())
False
```
###### 元组的不可变性
- 不可变指的是元组的内元素的值不可变
- 对于list等复杂数据类型的为引用方式存储数据类型的地址，其地址不可变，但内部数据可变
- count 计算tuple中存在相同元素的数量
- index 获取元素在tuple中的位置
- split 分割
```
>>> 'Name:dxy,Tel:182323xxxx,Age:21'.split(',')
['Name:dxy', 'Tel:182323xxxx', 'Age:21']
```
- flomat
    - 练习flomat 格式化输出
```python
users =[]

users.append((1,'zhang san ',29,'18231309230'))
users.append((1,'li si ',29,'18231309230'))
users.append((1,'wang wu',29,'18231309230'))
users.append((1,'liangliang',29,'18231309230'))

tuple_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
colums_title = ('ID', 'Name', 'Age', 'Tel')
tuple_body = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'
title = tuple_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3])
split_line ='-'*len(title)

print(split_line)
print(title)
print(split_line)

for i in users:
    print(tuple_body.format(i[0],i[1],i[2],i[3]))
print(split_line)
运行结果
---------------------------------------------
|    ID    |   Name   | Age |      Tel      |
---------------------------------------------
|    1     |zhang san | 29  |  18231309230  |
|    1     |  li si   | 29  |  18231309230  |
|    1     | wang wu  | 29  |  18231309230  |
|    1     |liangliang| 29  |  18231309230  |
---------------------------------------------
```
###### 练习代码：用户的管理（find/add/list/edit/delete)）

```python
users =[]

users.append((1,'zhang san ',29,'18231309230'))
users.append((2,'li si ',29,'18231309230'))
users.append((3,'wang wu',29,'18231309230'))
users.append((4,'liangliang',29,'18231309230'))
tuple_title = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
colums_title = ('ID', 'Name', 'Age', 'Tel')
tuple_body = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'
title = tuple_title.format(colums_title[0],colums_title[1],colums_title[2],colums_title[3])

split_line ='-'*len(title)
print(split_line)
print(title)
print(split_line)
for i in users:
    print(tuple_body.format(i[0],i[1],i[2],i[3]))
print(split_line)
'''
让用户从控制台输入format:name,age,tel
ID => 现有用户的最大ID + 1
'''
while True:
    input_do = input('请输入操作(find/add/list/edit/delete):')
    #输入等于list时，遍历当前users
    if input_do =='list':
        print(split_line)
        print(title)
        print(split_line)
        for i in users:
            print(tuple_body.format(i[0], i[1], i[2], i[3]))
        print(split_line)
    elif input_do == 'find':
        name = input('请输入查询的名字：')
        print(split_line)
        print(title)
        print(split_line)
        for user in users:
            if user[1] == name:
             print(tuple_body.format(user[0], user[1], user[2], user[3]))
        print(split_line)
    #添加用户
    elif input_do =='add':
        input_txt = input('请输入用户信息(Name,Age,Tel):')
        nodes = input_txt.split(',')
        if len(nodes) !=3:
            print('用户输入的信息错误！')
        else:
            uid = 0
            for user in users:
                if uid < user[0]:
                    uid = user[0]
            nodes[1] = int(nodes[1])
            # 类型转化需求一致
            users.append((uid + 1,) + tuple(nodes))
            print('添加用户成功！')
    #删除用户
    elif input_do=='delete':
        uid = input('请输入删除用户ID:')
        uid = int(uid)
        for user in users:
            if uid == user[0]:
                users.remove(user)
                break

    elif input_do =='edit':
        uid = input('请输入用户ID:')
        uid = int(uid)
        exist_user = None
        for user in users:
            if uid == user[0]:
                exist_user = user

                break
        if exist_user:
            txt = input('请输入用户信息:(name,age,tel)')
            nodes = txt.split(',')
            if len(nodes) != 3:
                print('输入信息错误')
            else:
                users.remove(exist_user)
                nodes[1] = int(nodes[1])
                users.append((uid,) + tuple(nodes))
            print(users)
        else:
            print('用户信息不存在')
```





















