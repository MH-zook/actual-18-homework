#users info dict,init is null
users = {}
ids = []
#format header
head_format = '|{0:<10}|{1:<5}|{2:<15}|{3:<20}'
title = ('ID','NAME','AGE','TEL')
body_format = '|{0:<10}|{1:<5}|{2:<15}|{3:<20}'
title_real = head_format.format(title[0],title[1],title[2],title[3])
#users add/delete/update/find/dict/exit
while True:
	v_input=input('please input add/delete/update/find/list/exit:')
	if v_input == 'add':
		v_input=input('please input name:age:phone separated by colon:')
		v_input.strip()
		if v_input.count(':')!=2:
			print('invalid input!')
			continue
		else:
			user,age,tel = v_input.split(':')[0],v_input.split(':')[1],v_input.split(':')[2]
		if not users:
			users[1] = {'name':user,'age':age,'tel':tel}
			print('1 record is added.')
		else:
			ids.clear()
			exist_flag = 0
			for key,value in users.items():
				if value['name'] == user:
					print('The user is existent.input again.')
					exist_flag = 1
				else:
					ids.append(key)
			if exist_flag == 0:
				users[max(ids)+1] = {'name':user,'age':age,'tel':tel}
				print('1 record is added.')
	elif v_input == 'delete':
		v_input_name = input('please input the username that you wanna delete:')
		key_flag = 0
		for key,value in users.items():
			if value['name'] == v_input_name:
				key_flag = key
		if not v_input_name:
			print('Input is empty and exit.')
		elif key_flag != 0:
			del users[key_flag]
			print('1 record is deleted')
		else:
			print('The user is nonexistent.')
	elif v_input == 'update':
		v_input = input('please input name:age:phone that you wanna update separated by colon:')
		if v_input.count(':')!=2:
                        print('invalid input!')
                        continue
		else:
			u_user,u_age,u_tel = v_input.split(':')[0],v_input.split(':')[1],v_input.split(':')[2]
		key_flag = 0
		for key,value in users.items():
			if value['name'] == u_user:
				key_flag = key
		if not v_input:
			print('Input is empty and exit.')
		elif key_flag != 0:
			users[key_flag] = {'name':u_user,'age':u_age,'tel':u_tel}
			print('1 record is updated.')
		else:
			print('The user is nonexistent.')
	elif v_input == 'find':
		v_input = input('please input the username that you wanna find:') 
		print(head_format.format(title[0],title[1],title[2],title[3]))
		print('-'*len(title_real))
		key_flag = 0
		for key,value in users.items():
			if value['name'] == v_input:
				key_flag = key	
		if key_flag != 0:
			print(body_format.format(key_flag,users[key_flag]['name'],users[key_flag]['age'],users[key_flag]['tel']))
			print('1 record is finded.')
		else:
			print('There is not record finded.')
	elif v_input == 'list':
		print(head_format.format(title[0],title[1],title[2],title[3]))
		print('-'*len(title_real))
		for key,value in users.items():
        		print(body_format.format(key,value['name'],value['age'],value['tel']))
	elif v_input == 'exit':
		print('bye bye!')
		break
	else:
		print('Invalid input!')
