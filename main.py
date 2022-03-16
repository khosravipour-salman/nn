from get_data import get_register_data, get_login_data
from account import register, login


while True:
	try:
		user_command = input('Enter 0 for Login; Enter 1 for Register; Enter q for quit; (0/1/q): ')
		if user_command == 'q':
			exit()

		elif user_command == '0':
			user_info = get_login_data()
			login(*user_info)
			
			while True:
				whats_next = input('Enter "info" for your full account information; "list" for user list; "q" for quit; ( info/list/q ): ')
				
				if whats_next == 'q':
					exit()

				elif whats_next == 'info':
					show_info()
					
				elif whats_next == 'list':
					show_user_list()

				else:
					raise ValueError(f'\n"{user_command}" is not recognized as an internal command.\n')		

		elif user_command == '1':
			user_info = get_register_data()
			register(*user_info)

		else:
			raise ValueError(f'\n"{user_command}" is not recognized as an internal command.\n')
	
	except ValueError as e:
		print(e)