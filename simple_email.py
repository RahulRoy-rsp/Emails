from conf_det import email_address,email_password

#pip install py3-validate-email
from validate_email import validate_email
import smtplib

sender = email_address
print(f"Sending email from {sender}")

def take_receivers_email_id():
    receiver = input("Enter receivers email address : ")
    isvalid = validate_email(email_address=receiver)
    if isvalid:
        print(f"Are you sure you want to send email to {receiver}(Y/N) ")
        inp = input().lower()
        if inp == 'y':
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender,email_password)
            message = input("Enter the Message you need to send : ")
            # sending a simple mail with just message ( no attachments and subject)
            s.sendmail(sender,receiver, message)
            print("Email sent Succesfully")
            s.quit()
            print("Exiting program ...")
        elif inp == 'n':
            take_receivers_email_id()
        else:
            print("Not a proper command given")
            print("Exiting program ...")
            pass
    else:
        print(f"{receiver} is not a valid email address")
        inp = input("Do you want to try again ? (Y/N)").lower()
        if inp == 'y':
            take_receivers_email_id()
        elif inp == 'n':
            print("Exiting program ...")
            pass
        else:
            print("Not a proper command given")
            print("Exiting program ...")
            pass

take_receivers_email_id()