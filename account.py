from users import users_list, add_user_to_file, get_user_by_username
from logger import log_user_register
from datetime import datetime


def register(username, password, fname, lname, city, email):
	add_user_to_file(username, password, fname, lname, city, email)
	log_user_register(username, datetime.now().replace(microsecond=0))


def login(username, password):
	if get_user_by_username(username):
		pass
		# check the password
		# if True: print(welcome)
		# if False: print(invalid credentials)
	print('User does not exist. ')
	