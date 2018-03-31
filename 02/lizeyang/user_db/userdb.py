# -*- coding:utf-8 -*-
#@Author: Lizeyang

'''
DESC:
----------------------------------------------
| ID |  NAME |  AGE  |   PHONE    |  DELETED |
----------------------------------------------
ID: 
    data_type=int  
    max_length=10
NAME:
    data_type=str 
    max_length=10
AGE:
    data_type=int
    max_length=3
PHONE:
    data_type=int 
    max_length=15
DELETED:
    data_type=bool
    max_length=5
    default=False
'''
from config import *

def red(mes):
    print("\033[1;31;40m" + mes + "\033[0m")

def green(mes):
    print("\033[1;32;40m" + mes + "\033[0m")


def insert():
    info = input("\033[1;31;40m请输入用户信息[name,age,phone]-->>>\033[0m ")
    id = users[len(users) - 1][0]
    id += 1
    name,age,phone = tuple(info.split(','))
    users.append([id,name,age,phone,deleted])
    green('用户%s,添加成功' %(name,))


def delete():
    user_name = input("\033[1;31;40m请输入要删除的用户名[name]-->>>\033[0m ")
    is_existed = False
    for user in users:
        if user[1] == user_name:
            is_existed = True
            user[4] = 'True'
            green("用户%s,删除成功" %(user_name,))
            break
    if not is_existed :
        red("用户%s,不存在" %(user_name,))

def restore():
    user_name = input("\033[1;31;40m请输入要恢复的用户名[name]-->>>\033[0m ")
    is_existed = False
    for user in users:
        if user[1] == user_name:
            is_existed = True
            user[4] = 'False'
            green("用户%s,恢复成功" %(user_name,))
            break
    if not is_existed :
        red("用户%s,不存在" %(user_name,))
        
        
def update():
    info = input("\033[1;31;40m请输入用户信息[old_name,new_name,age,phone]-->>>\033[0m ")
    #id = users[len(users) - 1][0]
    old_name,new_name,age,phone = tuple(info.split(','))
    is_existed = False
    for user in users:
        if user[1] == old_name:
            is_existed = True
            user[1] = new_name
            user[2] = age
            user[3] = phone
            green("用户%s,更新成功" %(new_name,))
            break
    if not is_existed :
        red("用户%s,不存在" %(old_name,))

def select(value):
    mes = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|{4:^10s}|'.format('ID','NAME','AGE','PHONE','DELETED')
    t_line = '-' * len(mes)
    green(t_line)
    green(mes)
    green(t_line)
    
    for i in users:
        if i[4] == value:
            id,name,age,phone,delet = i 
            mes1 ='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|{4:^10s}|'.format(str(id),str(name),str(age),str(phone),str(delet))
            green(mes1)
            t_line = '-' * len(mes1)
            green(t_line)
        elif value == 'all':
            id,name,age,phone,delet = i 
            mes1 ='|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|{4:^10s}|'.format(str(id),str(name),str(age),str(phone),str(delet))
            green(mes1)
            t_line = '-' * len(mes1)
            green(t_line)


def login():
    green("开始对数据库进行操作!")
    user = input("请输入数据库系统用户名 : ")
    if user == username:
        passwd = input("请输入数据库系统用户密码 : ")
        if passwd == password:
            green("[Login success! ] 开始对数据库进行操作!")
        else:
            red("[Error] 密码错误!")
            exit()
    else:
        red("[Error] 账号不存在!")
        exit()


