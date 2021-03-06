# <p align='center'> python day-01课后总结 </p>
![](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521476053082&di=ea5b7f843068f6ba60637b0d576f3a04&imgtype=0&src=http%3A%2F%2Ftc.sinaimg.cn%2Fmaxwidth.2048%2Ftc.service.weibo.com%2Fmmbiz_qpic_cn%2Fb8db78751723ccf9f58201a19f4ad54e.jpg)
### 课程的内容

### 什么是编程？
- 人和计算机之间交流的过程，为了使计算机能够理解人的意图，
- 必须将需解决的问题的思路、方法、和手段通过计算机能够理解的形式告诉计算机，
- 使得计算机能够根据人的指令一步一步去完成某种特定的任务
### 什么是python
- Python(蟒蛇)是一门简单易学, 优雅健壮, 功能强大, 面向对象的解释型脚本语言.
- 具有20+年发展历史, 成熟稳定. 具有丰富和强大的类库支持日常应用.
### python的特点
- 简单易学
- 优雅健壮
- 功能强大
- 面向对象
- 可移植
- 可扩展、可嵌入

### 准备python环境
- 版本：Python3.5
- python各个版本之间的有一定区别，尤其是2.7版本和3.X版本之间改动较多，Python2.7支持时间到2020年，使用新版本为趋势
- Python安装
- Linux(教学使用)
- 选择Ubuntu16.04，默认为Python3.5.2
- 使用系统软件管理工具apt/apt-get，yum等进行安装
- 使用源码安装
- Windows 下载地址：https://www.python.org/downloads/windows/


### 第一个Python程序
- 打开Python交互式环境
- 命令行中数据Python3.5版本程序名称
- 在Python交互式环境中输入print('Hello World')
- 在Python交互式环境中输入exit()
``` python
Python 3.5.4 (v3.5.4:3f56838976, Aug  7 2017, 12:56:33)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print('hello world')
hello world
>>> exit()
```
**1. 交互式运行环境备注---说明**
   - Linux命令行前缀为$或#，python交互式环境前缀为>>>
   - print为python的函数指令，用于让计算机打印括号中的内容
   - exit为python交互式环境下的函数指令，用于退出交互式环境

**2.交互式环境使用场景---问题**
   - exit后代码就没了（需要自己将代码保存到文件）
   - 每次需要重新输入（或者从文件中复制粘贴到python交互环境下运行）
   - 使用场景
   - 查看帮助信息
   - 快速测试

**3.脚本方式运行代码**
   - 编写python脚本
   - 创建.py后缀的文件（命名规则英文大、小写字母和数字，不能以数字开头）
   - 编辑文件内容print('Hello World')
   - 使用python3.5命令后加文件名方式运行文件
   - 代码注释，使用#开头

***练习：***
```python
print('Hello World'+'+'+ str(2))
print(2*3.1415926*10)
print(3.1415926*10*10)
print('100+2=',100 +2)
print('1-5 = ',1-5)
print('1*5 = ',1*5)
print('1/5 = ',1/5)

-》结果输出

Hello World+2
62.831852
314.15926
100+2= 102
1-5 =  -4
1*5 =  5
1/5 =  0.2
```

### 变量&语句
***变量定义&赋值***
```python
a_pi = 3.1415926
ra = 10
print (2*a_pi*ra)
print(a_pi*ra*ra)

输出结果：
62.831852
314.15926
```

定义变量
```python
pi=3.1415926
area = pi * radius ** 2
```
注：变量命名规则：
* 只能由大小写英文字母、数字、下划线组成
* 不能以数字开头
* 避免和python保留字和关键字冲突
* 变量名先定义，后使用


### 3. 数据类型
整数、浮点数、正数、负数
- ***按是否带小数点***
   - 整数
   - 浮点数
- ***按是否带负号***
    - 正数
    - 负数
```python
像年龄、身高、体重、分数、圆周率这样的数字
height = 1.71
age =29
wiht =140
pi = 3.1415926
score = 5.5
```
数据类型的运算---四则运算
1. 加(+)、减(-)、乘(*)、除(/)、整除(//)、余(%)、幂(**)
* 加(+)
    - 必须两个字符串相加
* 乘(*)
    - 必须为一个整数
* 除(/)
    - 不能与0相除
类型的判断与转换

* type 函数判断类型
```python
print(type(1))
print(type(1.0))
print(type(''))

type结果：
<class 'int'>
<class 'float'>
<class 'str'>
```
* 类型相互转化
    - int/str => float
    - float/str => int
    - int/float => str
```python
print(type(int(1.9)))
print(type(int(2)))
print(type(float(1)))
print(type(str(1)))
print(type(str(1.8)))

类型输出结果
<class 'int'>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'str'>
```

### 4. 数字字符串、布尔类型
字符串类型
使用单引号、双引号、三个单引号或三个双引号引起来的一些字符
name = 'dxy'
job = "linux"
特殊字符
 \     转义符
\r 回车
\n     换行
\t     tab键
\f     换页
```python
print("i 'm dxy")
print('i\'m dxy')
print('a \nb \tc ')
print('a\\nb\\tc\\')
```
```
练习
name = str('dxy')
age = int('20')

input('please name and age->:')
print('My name is',name,'Im,',age,'years old')
```
* 布尔类型
- 表示真假，只有True/False两个值
- 布尔运算
    - 或 (A or B：A、B两个只要一个为真则为真)
    - 且 (A and B：A、B两个都为真时才为真
    - 非 (not A： A为真则为假，A为假则为真)
- 四则运算
    - 加(类似or)、减、乘(类似and)、除
    - 类型转换
    - int/str/float => bool  (练习0, 1, -1, 0.0, 0.1, 0.2, ‘a’, ‘’)
    - bool => int/str/float



### 5. 流程控制
### 6. 条件语句
- 根据表达式的真假控制代码的执行流程
- 关键字if, elif, else
- 条件表达式使用:标识条件结束，子语句开始
- 使用缩进(建议4个空格)表示子语句
- 从第一个条件开始判断，如果条件为真则执行子语句，否则判断下一个条件，如果所有为假，则执行else中的子语句
- elif可以有0个或任意多个，else可以有0个或一个
- 提示用户从控制台输入一个分数

* 练习一个笑话的条件语句
程序员的妻子叫程序员去买一斤包子，如果看到卖西瓜的，买一个。
一会儿，程序员拿着一个包子回来了，
妻子问他为什么只买一个包子，答曰：看到卖西瓜的了。
- 伪代码：
    - 妻子
        - 买一斤包子，如果看到西瓜，就买一个西瓜
    - 丈夫
        - 如果看到西瓜就买一个包子，否则就买一斤包子

```python
#妻子的想法
momeny = 100
prompt = input('看到卖西瓜的了吗？(Y/N)')

if prompt =='Y':
    print('买一斤包子需要花费：10元')
    momeny -= 10
if prompt =='Y':
    print('买一个西瓜需要花费：20元')
    momeny -= 20
print('剩余金额'+ str(momeny))

#老公想法
momeny =100
prompt1 = input('看到卖西瓜的了吗？(Y/N)')

if prompt1 == 'Y':
    print('买一个包子需要：3元')
    momeny -= 3
else:
    print('买一斤包子需要：10元')
    momeny -= 10
print('剩余金额'+str(momeny))
```

### 7. 循环语句
根据表达式的真假控制代码的是否结束子语句循环执行，如果为真则继续循环执行
* 计算1-100的和
```python
total = 0
idx = 1
while idx <= 100:
    total = total+ idx
    idx = idx+1

print(total)

```
练习
1. 循环提示用户在控制台上输入数字或者exit，当用户输入exit后结束程序，并打印所有输入数字的和与平均数
```python
total = 0
count = 0
input_number = ''

while input_number !='exit':
    input_number = input('请输入一个数字--：')
    if input_number != 'exit':
        total += float(input_number)
        count += 1

if count !=0:
    print('total',total,'avg',total/count)
else:
    print('total:', total, ', avg:', 0)
```
### 8. continue&break
break 跳出循环
continue 跳过本次循环，继续下一次循环条件判断
```python
idx = 0
while idx <= 10:
    idx += 1
    if idx == 4:
        continue
    else:
        if idx ==9:
            break
    print(idx)
```
 - 有序的数据集合
    - nums = [1, 5, 6, 3, 2, 5]
    - 获取序列中第n个元素
    - nums[n - 1]
 - 遍历集合中所有元素
- 有序的数据集合
```python
nums = [1, 5, 6, 3, 2, 5]
for  nums1 in nums:
    print(nums1)
```
作业
打印乘法口诀
提示：尝试print(‘kk’)与print(‘kk’, end=‘’)的区别
```python
x = 0
while x <9:
    x += 1
    # print(x)
    y=0
    # print(y)
    while y < x:
        y += 1
        print("%d*%d=%2d" % (x,y,x*y),end=" ")
    print('\n')
```
- 猜数游戏
    - 随机生成一个0到100的数字，提示用户在控制台上输入一个数字
    - 当用户输入数字小于生成的随机数，则打印猜小了
    - 当用户输入数字大于生成的随机数，则打印猜大了
    - 当用户输入数字等于生成的随机数，则打印猜对了，结束程序
    - 用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序
提示：生成随机数的方法
import random
```python
import random
num_random = random.randint(0,100)
count = 1
while True:
    input_num = int(input('游戏限制输入5次结束，请慎重输入>>'))
    if input_num ==num_random:
        print('高手！猜对了')
        break
    elif input_num > num_random:
        print('猜大了！！小伙伴')
    else:
        print('猜小了！！小伙伴')
    count =count+1
    if count > 2:
        print('太笨了，下次再来，正确的数字是',int(num_random))
        break

```




