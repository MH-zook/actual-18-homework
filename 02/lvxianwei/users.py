users=[]
users.append((1,"lvxianwei",30,"158********"))
users.append((2,"lvxianjun",38,"186********"))
users.append((3,"lvfanju",64,"186********"))

infm_user="|{0:^10s}|{1:^12s}|{2:^5s}|{3:^15s}|"
infm_user_head=("ID","Name","Age","Tele")
users_body="|{0:^10d}|{1:^12s}|{2:^5d}|{3:^15s}|"



while True:
    operate=input("请选择您要进行的操作add/delete/check/fix/list/quit:")
    if operate=="add":
        #增
        add_text=input("请输入您的个人信息（格式为：“姓名，年龄，电话号码”):")
        add=add_text.split(",")
        users.append((len(users)+1,add[0],int(add[1]),add[2]))
    if operate=="list":
        #显示用户列表
        print("-"*len(infm_user))
        print(infm_user.format(infm_user_head[0],infm_user_head[1],infm_user_head[2],infm_user_head[3]))
        print("-"*len(infm_user))
        for user in users:
            print(users_body.format(user[0],user[1],user[2],user[3]))
    if operate=="check":
        #查
        check_name=input("请输入您的姓名:") 
        idx=0
        for user in users:
            if check_name==user[1]:
                print(infm_user.format(infm_user_head[0],infm_user_head[1],infm_user_head[2],infm_user_head[3]))
                print(users_body.format(user[0],user[1],user[2],user[3]))
                break
            idx+=1
        if idx==len(users):#如果用户不再列表，打印提示
            print("很抱歉！您还不是我们的用户，期待您的加入！")
    if operate=="delete":
        #删
        del_name=input("请输入您要注销的用户名:") 
        idx=0
        for user in users:
            if del_name==user[1]:
                users.remove(user)
                print("已删除")
                break
            idx+=1
        if idx==len(users)+1:#如果用户不再列表，打印提示
            print("很抱歉！你输入的用户不存在或已注销！")
    if operate=="fix":
        #改
        fix_name=input("请输入您要修改信息的用户名:") 
        idx=0
        for user in users:
            if fix_name==user[1]:
                ID=user[0]
                users.remove(user)
                add_text=input("请输入修改后的个人信息（格式为：“姓名，年龄，电话号码”):")
                add=add_text.split(",")
                users.append((ID,add[0],int(add[1]),add[2]))
                print("已修改")
                break
            idx+=1
        if idx==len(users)+1:#如果用户不再列表，打印提示
            print("很抱歉！你输入的用户不存在，请重新查正！")
        if len(users)>=2:
            for j in range(len(users)-1):
                for i in range(len(users)-1):
                    if int(users[i+1][0])<int(users[i][0]):
                        user=users[i]
                        users[i]=users[i+1]
                        users[i+1]=user

    if operate=="quit":
        #结束
        break
    if operate!="add" and operate!="list" and operate!="quit" and operate!="check" and operate!="fix" and operate!="delete":
        print("操作不合法，请重新输入！")