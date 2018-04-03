# encoding: utf-8
# Author: LW
"""

user = {
    1 : {name:kk, age:30, tel: 158xxxxx},
    2 : {name:kk2, age:30, tel: 158xxxxx},
    3 : {name:kk3, age:30, tel: 158xxxxx},
    4 : {name:kk4, age:30, tel: 158xxxxx},
}

list=>显示所有
提示用户输入排序字段(id,name,age,tel)

find=>查找
提示用户输入查找字符串，罗列name和tel中包含字符串的所有数据

添加和修改的 检查用户名不能重复
age类型检查，所有数据strip()、

输入exit退出

"""

# 初始化用户清单
users = {
    4: {'name': 'kk1', 'age': 28, 'tel': '158xxxx7'},
    3: {'name': 'kk2', 'age': 29, 'tel': '158xxxx2'},
    2: {'name': 'kk3', 'age': 30, 'tel': '158xxxx9'},
    1: {'name': 'kk4', 'age': 31, 'tel': '158xxxx1'}
}
# 初始化列表标题
title = ('Id', 'Name', 'Age', 'Tel')
format_str = '|{0[0]:^10d}|{0[1][name]:^20s}|{0[1][age]:^10d}|{0[1][tel]:^24s}|'
format_title = '|{0[0]:^10s}|{0[1]:^20s}|{0[2]:^10s}|{0[3]:^24s}|'
# 将title元组直接进行格式转换
title_str = format_title.format(title)
# 定义分割线
split_line = '-' * len(title_str)


#  打印初始化信息
def print_welcome_info():
    print('*********************************************************************')
    print('*                     Welcome to User Management                    *')
    print('*        You can select a menu number to choose an operation        *')
    print('*********************************************************************')


# 打印菜单方法
def print_menu():
    # 以下在屏幕上直接输出与定义的菜单
    # 采用此方式是为了避免用户输入过多内容可能引起的输入错误
    # 用户通过输入菜单编号访问相关功能，既方便又能减少失误
    print('---------------------------Menu List---------------------------------')
    print("-\t1. List Users.")
    print("-\t2. Add User.")
    print("-\t3. Delete User.")
    print("-\t4. Edit User.")
    print("-\t5. Find User.")
    print("-\t0. Exit System.")
    print('---------------------------------------------------------------------')


# 打印全部用户列表方法
def print_user_list(print_list):
    # 打印分割线
    print(split_line)
    # 打印列表标题行
    print(title_str)
    # 打印分割线
    print(split_line)
    # 如果users list 中有记录，则遍历users list ，逐条输出到屏幕上
    if len(print_list) > 0:
        # 遍历users list
        for user in print_list.items():
            print(format_str.format(user))
    # 如果users list中无记录，则直接输出一行'no user yet!' 提示用户没有相关记录
    else:
        print('                   no user yet!')
    # 打印分割线
    print(split_line)


def check_name_exist(user_id, user_name):
    is_exist = False
    for key, user in users.items():
        if key == user_id:
            continue
        else:
            if user.get('name') == user_name.strip():
                is_exist = True
                break
    return is_exist


def add_user():
    while True:
        insert_info = input('请输入增加的用户信息（Name,Age,Tel）：')
        insert_user_tmp = insert_info.split(',')
        if len(insert_user_tmp) != 3:
            print('输入的数据格式有误，请重新输入！')
            continue
        if not insert_user_tmp[1].strip().isdigit():
            print('年龄必须为数字，请重新输入！')
            continue
        insert_user_tmp[1] = int(insert_user_tmp[1].strip())
        if insert_user_tmp[1] <= 0:
            print('年龄必须大于0岁，请重新输入！')
            continue
        max_id = 0
        if check_name_exist(max_id, insert_user_tmp[0]):
            print('用户姓名重复，请重新输入！')
            continue
        if len(users) == 0:
            max_id = 1
        else:
            max_id = max(users) + 1
        users[max_id] = {'name': insert_user_tmp[0].strip(), 'age': insert_user_tmp[1],
                         'tel': insert_user_tmp[2].strip()}
        print_user(max_id)
        break
    input('用户添加成功，任意输入按下回车返回菜单：')


def mod_user():
    if len(users) == 0:
        print("目前没有记录，不能做修改操作! ")
        return
    print_user_list(users)

    while True:
        mod_id = input('请输入要修改的用户ID,如需要返回菜单请输入Q：')
        if mod_id.upper() == 'Q':
            break
        if not mod_id.strip().isdigit():
            print("输入内容错误，ID必须为整数! ")
            continue
        mod_id = int(mod_id.strip())
        if mod_id not in users.keys():
            print("输入ID不存在，请重新输入! ")
            continue
        print_user(mod_id)
        while True:
            edit_info = input('上方为要修改的用户信息，请输入修改信息（Name,Age,Tel）,如需要返回菜单请输入Q：')
            if edit_info.upper() == 'Q':
                break
            edit_user_tmp = edit_info.split(',')
            if len(edit_user_tmp) != 3:
                print('输入的数据格式有误，请重新输入！')
                continue
            if not edit_user_tmp[1].strip().isdigit():
                print('年龄必须为数字，请重新输入！')
                continue
            edit_user_tmp[1] = int(edit_user_tmp[1].strip())
            if edit_user_tmp[1] <= 0:
                print('年龄必须大于0岁，请重新输入！')
                continue

            if check_name_exist(mod_id, edit_user_tmp[0]):
                print('用户姓名重复，请重新输入！')
                continue

            users[mod_id] = {'name': edit_user_tmp[0].strip(), 'age': edit_user_tmp[1],
                             'tel': edit_user_tmp[2].strip()}
            input('用户修改成功，任意输入按下回车返回菜单：')
            break
        break


def del_user():
    if len(users) == 0:
        print("目前没有记录，不能做删除操作! ")
        return
    print_user_list(users)

    while True:
        delete_id = input('请输入要删除的用户ID：')
        if not delete_id.isdigit():
            print("输入内容错误，必须为整数! ")
            continue
        delete_id = int(delete_id)
        if delete_id not in users.keys():
            print("输入ID不存在，请重新输入! ")
            continue
        print_user(delete_id)
        delete_confirm = input('上方为要删除的用户信息，确认删除请输入Y，否则直接输入回车返回菜单：')
        if delete_confirm.upper() == 'Y':
            del users[delete_id]
            input('用户ID：' + str(delete_id) + ' 删除成功，任意输入按下回车返回菜单：')
            break
        else:
            print("选择了否，取消删除操作，任意输入按下回车返回菜单：")
            break


def search_user():
    while True:
        conditions = input('请输入关键字进行检索，输入Q退出检索：')
        if conditions.strip().upper() == 'Q':
            break
        if conditions.strip() == '':
            print("检索条件不能为空,请重新输入! ")
            continue
        search_users_list = {}
        for key, user in users.items():
            if user.get('name').find(conditions.strip()) != -1 or user.get('tel').find(conditions.strip()) != -1:
                search_users_list[key] = user

        print_user_list(search_users_list)
        return_code = input('查询完成， 输入S重新检索，任意输入按下回车返回菜单：')
        if return_code.strip().upper() == 'S':
            continue
        else:
            break


def list_user():
    print_user_list(users)
    while True:
        op_code = input('输入（id,name,age,tel）进行字段排序,任意输入按下回车返回菜单：')
        sort_users_tmp = {}
        if op_code.strip().upper() == 'ID' or op_code.strip().upper() == 'NAME' or op_code.strip().upper() == 'AGE' or op_code.strip().upper() == 'TEL':
            sort_users_tmp_list = []
            for k, v in users.items():
                users_tuple = (k, v.get('name'), v.get('age'), v.get('tel'))
                sort_users_tmp_list.append(users_tuple)
            sort_idx = 0
            if op_code.strip().upper() == 'ID':
                sort_idx = 0
            elif op_code.strip().upper() == 'NAME':
                sort_idx = 1
            elif op_code.strip().upper() == 'AGE':
                sort_idx = 2
            else:
                sort_idx = 3
            sort_users_tmp_list = sorted(sort_users_tmp_list, key=lambda s: s[sort_idx])
            for x in sort_users_tmp_list:
                sort_users_tmp[x[0]] = users.get(x[0])
            print_user_list(sort_users_tmp)
        else:
            break


# 打印单个用户方法
def print_user(id):
    # 打印分割线
    print(split_line)
    # 打印列表标题行
    print(title_str)
    # 打印分割线
    print(split_line)
    # 根据传入的参数user对象，打印一行数据
    user = (id, users.get(id))
    print(format_str.format(user))
    # 打印分割线
    print(split_line)


#  打印退出信息
def print_exit_info():
    print('*********************************************************************')
    print('*                 Good bye and see you next time!                   *')
    print('*********************************************************************')


# 主函数
def main():
    print_welcome_info()
    while True:
        print_menu()
        operation_code = input('请输入菜单序号，选择需要进行的操作：')
        if not operation_code.isdigit():
            print("输入内容错误，必须为菜单序号：1, 2, 3, 4, 5 或者 0 ")
            continue
        operation_code = int(operation_code)

        if operation_code == 0:  # 选择0，则退出
            break
        elif operation_code == 1:  # 选择1，进入列表
            list_user()
        elif operation_code == 2:  # 选择2，进入增加用户功能
            add_user()
        elif operation_code == 3:  # 选择3，进入删除用户功能
            del_user()
        elif operation_code == 4:  # 选择4，进入修改用户功能
            mod_user()
        elif operation_code == 5:  # 选择5，进入查找用户功能
            search_user()
    print_exit_info()


if __name__ == '__main__':
    main()
