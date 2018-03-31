#encoding: utf-8

users = []

users.append((1, 'kk', 29, '185xxxxxx'))
users.append((2, 'wd', 28, '186xxxxxx'))
users.append((3, 'woniu', 30, '187xxxxxx'))

'''
10s   10s    5s     15s
| ID | 姓名 | 年龄 | 联系方式 |
------------------------------------
|1|kk|29|185

'''

while True:

    tpl_tital = '|{0:^10s}|{1:^10s}|{2:^5s}|{3:^15s}|'
    tital_name = ('ID','Name','Age','Tel')

    tpl_columns = '|{0:^10d}|{1:^10s}|{2:^5d}|{3:^15s}|'
    tital = tpl_tital.format(tital_name[0],tital_name[1],tital_name[2],tital_name[3])

    op = input('请输入操作(list/add/delete/edit):')

    if op == 'exit':
        print('退出！')
        break

    if op == 'list':



        print(tital)
        print('-'*len(tital))

        for user in users:
            print(tpl_columns.format(user[0],user[1],int(user[2]),user[3]))

        print('-'*len(tital))

    elif op == 'add':

        prompt = input('请输入用户信息name,age,tel:')

        new_user = prompt.split(sep=',')

        max_id = 1

        for user in users:
            if user[0] > max_id:
                max_id = user[0]

        max_id += 1

        new_user.insert(0,max_id)

        users.append(tuple(new_user))

    elif op == 'delete':

        prompt = input('请输入删除用户的名字name:')

        for user in users:

            if prompt in user:
                users.remove(user)

    elif op == 'edit':

        username = input('请输入用户名字name:')
        user_id =0
        for user in users:

            if username in user:

                user_id = user[0]
                print(tpl_columns.format(user[0],user[1],int(user[2]),user[3]))
                new_info = input('请输入新的用户信息age,tel:').split(sep=',')
                edit_users = [user_id,username] + new_info
                users.remove(user)
                users.append(tuple(edit_users))
                break
    else:
        print('输入错误，退出！')
        break






