# encoding: utf-8
# author: niko
# ver2.0 : 修改users为字典，输入剔除前后空格，输入数据进行类型鉴别，表格更新后进行排序，无法新建name相同的用户
# last_time:2018/4/2 15:12


#初始数据
users = {
    1 : {'name':'kk1', 'age':30, 'tel': '158xxxxx'},
    2 : {'name':'kk2', 'age':30, 'tel': '158xxxxx'},
    3 : {'name':'kk3', 'age':30, 'tel': '158xxxxx'},
    4 : {'name':'kk4', 'age':30, 'tel': '158xxxxx'},
}


'''
---------------------
|id|name|age|contact|
---------------------
|01| kk | 28|138xx00|
---------------------
'''
#定义头部
_per_Title = '|{0:^3s}|{1:^10s}|{2:^5s}|{3:^13s}|'
_title = _per_Title.format('id','name','age','contact')
_line = '-' * len(_title)
_per_body = '|{0:^3d}|{1:^10s}|{2:^5d}|{3:^13s}|'

def _banner():
    _welcome ='|welcome to using usmgr system|'
    print('-'*len(_welcome))
    print('|'+' '*(len(_welcome)-2)+'|')
    print(_welcome)
    print('|'+' '*(len(_welcome)-2)+'|')
    print('-'*len(_welcome))
_banner()

while True:
    #排序
    users=dict(sorted(users.items(),key=lambda e:e[0]))
    _fun = input('请输入以下指令 find/list/add/delete/update/exit:').strip()
    #listuser
    if _fun == 'list':
        print(_line)
        print(_title)
        print(_line)
        for user in users.items():
            print(_per_body.format(user[0],user[1].get('name'),user[1].get('age'),user[1].get('tel')))
        print(_line)

    #adduser
    elif _fun == 'add':
        add_user = input('请输入相关信息 name,age,contact:').strip()
        nodes = add_user.split(',')
        name_exist = None

        for user in users.items():
            if nodes[0] == user[1].get('name'):
                name_exist = user[1].get('name')

        if len(nodes) != 3:
            print('你输入的信息有误，请重新输入。')
        elif nodes[1].isdecimal is False:
            print('你输入的年龄不是数字，请重新输入。')
        elif name_exist != None:
            print('你输入了的名字已存在，请重新输入！')
        else:
            uid = 0
            for user in users.items():
                if uid < user[0]:
                    uid = user[0]
            nodes[1] = int(nodes[1])
            users.update({uid+1:{'name':nodes[0],'age':nodes[1],'tel':nodes[2]}})
    #delete
    elif _fun == 'delete':
        uid_user = int(input('请输入你要删除的用户ID: ')).strip()
        for user in users.items():
            if uid_user == user[0]:
                del users[uid_user]
                break
    #find
    elif _fun == 'find':
        exist_user = None
        find_text = (input('请输入你要查询的用户信息 name/contact: ')).strip()
        for user in users.items():
            if find_text in str(user[1].get('name')) or find_text in str(user[1].get('tel')):
                exist_user = _per_body.format(user[0],user[1].get('name'),user[1].get('age'),user[1].get('tel'))
                print(exist_user)

        if exist_user == None:
            print('用户信息不存在')
    #update
    elif _fun == 'update':
        find_text = (input('请输入你要修改用户的name: ')).strip()
        exist_user = None
        for user in users.items():
            if find_text == user[1].get('name'):
                exist_user = _per_body.format(user[0],user[1].get('name'),user[1].get('age'),user[1].get('tel'))
            if exist_user:
                print('你要修改的用户是',end='\t')
                print(exist_user)
                update_user = input('请重新输入该用户信息 name,age,contact: ').strip()
                nodes = update_user.split(',')
                if len(nodes) != 3:
                    print('你输入的信息有误。')
                else:
                    nodes[1] = int(nodes[1])
                    uid = user[0]
                    del users[user[0]]
                    users.update({uid:{'name':nodes[0],'age':nodes[1],'tel':nodes[2]}})
                    print('修改成功')
                    break
        if exist_user == None:
            print('用户信息不存在')
    #exit
    elif _fun == 'exit':
        _exit = input('是否如确认退出程序 yes/no？').strip()
        if _exit == 'yes':
            break
        else:
            continue
