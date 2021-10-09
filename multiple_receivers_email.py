from confidential_data import email_address,email_password
import smtplib
from validate_email import validate_email

sender = email_address
print(f"Sending email from {sender}")

email_list = []
message = input("Please enter the message you want to send to the receipents : ")

def send_message():
	global message
	for receiver in email_list:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(sender,email_password)
		message = message
		s.sendmail(sender,receiver, message)
		s.quit()
	print(f"Email sent Succesfully to {email_list}")
	print("Exiting program ...")

def try_more():
	inp = input("Do you want to add more email address(Y?N) : ")
	if inp == 'y':
		take_receivers_email_id()
	elif inp == 'n':
		send_message()
	else:
		print(f"Invalid command ({inp}) given :")
		print("sending email")
		send_message()

def take_receivers_email_id():
	receiver = input("Enter the email addresses you want to send message : ")
	isvalid = validate_email(email_address=receiver)
	if isvalid:
		if receiver in email_list:
			print(f"{receiver} is already in the list")
			try_more()
		else:
			print(f"{receiver} added successfully to the list :")
			email_list.append(receiver)
			try_more()
	else:
		print(f"{receiver} is not a valid email address")
		inp = input("Do you want to try again ? (Y/N)").lower()
		if inp == 'y':
			take_receivers_email_id()
		elif inp == 'n':
			if email_list == []:
				print("Exiting program ...")
			else:
				send_message()
		else:
			print("Not a proper command given")
			print("Exiting program ...")
			pass

take_receivers_email_id()
