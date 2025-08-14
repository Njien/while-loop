ussd = "*555#"
balance = 1000
phone_number = int(input("Enter phone number:\n>>> "))
enter_ussd = input("Enter USSD to continue:\n>>> ")
SHOULD_EXECUTE = True
while SHOULD_EXECUTE:
	#	balance = 1000
#	phone_number = int(input("Enter phone number:\n>>> "))
#	enter_ussd = str(input("Enter USSD to continue:\n>>> "))
	if enter_ussd == ussd:
		options = ["buy data", "buy airtime", "check balance", "exit"]

		print("""AVAILABLE OPTIONS:
		1. Buy Data
		2. Buy airtime
		3. Check balance
		4. Exit
		""")
		enter_choice = int(input("Enter choice from the above options:\n>>> "))

		if enter_choice == 1:
			print(options[0])
			data_plan = {"1gb": 300, "2GB": 600, "3.5GB":  1000}
			print("""AVAILABLE PLANS:
			1. 1GB @ 300
			2. 2GB @ 600
			3. 3.5GB @ 1000""")
			data_balance = int(input("enter choice from the above:\n>>> "))

			if data_balance == 1:
				if  data_plan["1gb"] <= balance:
					
					print(f"You have successfully purchase 1gb on {phone_number}\nThank you for choosing MTN")
					balance = balance - data_plan["1gb"]
					print(f"Your remaing balance is: {balance}")
				else:
					print(f"insufficient balance:\nAvaialble balance is:{balance}")

			elif  data_balance == 2:
				if  data_plan["2GB"] <= balance:
					print(f"You have successfully purchase 2gb on {phone_number}\nThank you for choosing MTN")
					balance = balance - data_plan["2GB"]
					print(f"Your remaing balance is: {balance}")
				else:
					print(f"insufficient balance:\nAvaialble balance is:{balance}")
			elif data_balance == 3:
				if  data_plan["3.5GB"] <= balance:
					print(f"You have successfully purchase 3gb on {phone_number}\nThank you for choosing MTN")
					balance = balance - data_plan["3.5GB"]
					print(f"Your remaing balance is: {balance}")

			else:
				print("invalid options")
		elif enter_choice == 2:
			print(options[1])
			
			airtime_amount = int(input("Enter amount"))
			if airtime_amount <= balance:
				 print(f"You have successfully purchase airtime of {airtime_amount} on {'phone_number'}\nThank you for choosing MTN")
				 balance = balance - airtime_amount
				 print(f"Your remaing balance is: {balance}")
			else:
				 print(f"insufficient balance:\nAvaialble balance is:{balance}")
		elif enter_choice == 3:
			print(options[2])

			print(f"Your Available balance is: {balance}")
		elif enter_choice == 4:
			SHOULD_EXECUTE = False
			print("Good bye!")
		else:
			print("invalid option..\nTry againlater")
	else:
		print("invalid ussd")
