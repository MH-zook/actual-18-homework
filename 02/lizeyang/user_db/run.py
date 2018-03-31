from config import *
from userdb import *



if __name__ == '__main__':
	login()
	while True:
	    op = input("\033[1;31;40m请输入要执行的操作-->>>[add/del/update/sel/sel_all/sel_del/rest]-->>> \033[0m ")
	    if op == 'sel':
	        select('False')
	    elif op == 'sel_del':
	        select('True')
	    elif op == 'sel_all':
	        select('all')
	    elif op == 'add':
	        insert()
	    elif op == 'del':
	        delete()
	    elif op == 'rest':
	    	restore()
	    elif op == 'update':
	        update()
	    elif op == 'exit':
	        green("退出成功！")
	        break