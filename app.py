#Code to run the python email automation
import os
import smtplib,ssl
import imghdr
from email.message import EmailMessage
port = 465
smtp_server ='smtp.gmail.com'

sender_email='zeeshankhan29khan@gmail.com'
password ='ahvyhvntqgwejqqv'

reciever_email =["zeeshankhan29khan@gmail.com","faizankhan29khan@gmail.com"]

subject ='check'
body ='''Hi,

This email is sent automatically by running python script.


Thanks and Regards
Zeeshan khan
Jr.Datscientist

'''

em = EmailMessage()
em['subject'] = subject
em.set_content(body)

files =['test.csv']
for file in files:
    with open(file,'rb') as f:
        file_name = f.name
        file_data = f.read()
        em.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,em.as_string())
    print('Email sent succesfully')