users_list = {
	'username1': {
		'password': 'passwd',
		'first_name': 'test_first_name',
		'last_name': 'test_last_name',
		'city': 'tehran',
		'email': 'myemail@gmail.com',
	},
	'username2': {
		'password': 'passwd2',
		'first_name': 'test_first_name2',
		'last_name': 'test_last_name',
		'city': 'shiraz',
		'email': 'username@gmail.com',
	},
}


def show_user_list():
	pass


def show_info():
	pass


def add_user_to_file(username, password, fname, lname, city, email):
	handler = open('users.txt', 'a')
	handler.write(f'###username={username}@@password={password}@@fname={fname}@@lname={lname}@@city={city}@@email={email}')
	handler.close()
	

def get_users():
	handler = open('users.txt', 'r')
	raw_file_data = handler.read()
	users = raw_file_data.split('###')
	users_dict = {}
	# for user in users:
	# 	u = user.split('@@')
	# 	users_dict[f'{u[0]}'] = {}

	# 	for i in u:
	# 		users_dict[u[0]] = i.split('=')[0]: i.split('=')[1]
		

		# users_dict = {f'{info[0]}': {'password': info[1], 'fname': info[2], 'lname': info[3], 'email': info[4]}}
	print(users_dict)
	# convert string to the desired dict
	# return the dictionary
	


def get_user_by_username(username):
	get_users()
	# return a specific user
	# run get users
	# get a specific user from dict
	# return the user