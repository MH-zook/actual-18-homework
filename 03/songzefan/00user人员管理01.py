#!/usr/bin/env python3
# encoding: utf-8

users={}

text= """ ----用户管理系统 V-1.0.0----
        请按提示进行输入要执行的操作
          add :   添加用户
          del :   删除用户
          update: 编辑用户信息
          list:   列出用户信息
          find:   查找用户
          exit/q: 退出系统
"""

print(text)

while True:
    INPUT=input('请输入要执行的操作：')
    per={}
    
    if INPUT == "add":
        new_user=input("请输入用户信息格式(用户名:年龄:联系方式): ").strip()
        if new_user.split(':')[0] in users.keys():
            print("此用户已经存在！！！")
        #    continue
        else:
            per['name']= new_user.split(":")[0]
            per['age']= int(new_user.split(":")[1])
            per['tel']= new_user.split(":")[2]
            users[per['name']]=per
            print('用户添加成功！！！')
            print(users)

    if INPUT == "del":
        input_txt=input("请输入要删除的用户名：")
        if input_txt in users.keys():
            del users[input_txt]
        else:
            print("此用户不存在！！！")

    if INPUT == "update":
        new_user=input("请输入要更新的用户信息，格式(用户名:年龄:联系方式): ")
        if new_user.split(':')[0] not in users.keys():
            print("此用户不存在！！！")
         #   continue
        else:
            users[new_user.split(':')[0]]['nme']=new_user.split(':')[0]
            users[new_user.split(':')[0]]['age']=int(new_user.split(':')[1])
            users[new_user.split(':')[0]]['tel']=new_user.split(':')[2]

    if INPUT == "find":
        input_txt=input("请输入要查找的用户名：")
        if input_txt not in users.keys():
            print("此用户不存在！！！")
        else:
            print("|{0:^10s}|{1:^5s}|{2:^15s}|".format("姓名","年龄","联系方式"))
            print("|{0:^10s}|{1:^5d}|{2:^15s}|".format(users[input_txt]['name'],users[input_txt]['age'],
            users[input_txt]['tel']))

    if INPUT == "list":
        print("|{0:^10s}|{1:^5s}|{2:^15s}|".format("姓名","年龄","联系方式"))
        print('-'*40)
        for i in list(users.items()):
            print("|{0:^10s}|{1:^5d}|{2:^15s}|".format(i[0],i[1]['age'],i[1]['tel']))

    if INPUT == "exit" or INPUT == "q":
        print('谢谢使用！！！')
        break
