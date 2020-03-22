import smtplib

sender = 'xxxxxxxxxx'
pswd = "xxxxxxxxxxxx"
reciever = 'xxxxxxxx'

message = """
This message is for
testing purpose only
hence, DO NOT PANIC !!!
"""

# creates SMTP session
smtp_Obj = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
smtp_Obj.starttls()

# Authentication
smtp_Obj.login(sender, pswd)

# sending the mail
smtp_Obj.sendmail(sender, reciever, message)

# terminating the session
smtp_Obj.quit()

print("mail has been successfully sent to \"", reciever, "\"")
