import os
from email.mime.multipart import MIMEMultipart, MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib


names= ['Jerome']

#build message contents

msg=MIMEMultipart('related')
msg['Subject']='Btw this is made through automation with python lol'
msg.attach(MIMEText("If you're reading this, you're lame!"))

#initialize connection to our email server, we will use gmail here
smtp= smtplib.SMTP('smtp.gmail.com', port='587')

smtp.ehlo() # send the extended hello to our server
smtp.starttls() # tell server we want to communicate with tls encryption

smtp.login('jcala0509@gmail.com', 'fasdl;fkjasd;f!') #login to our email server (dummy password, enter your own login information to test)

#send our email message  'msg' to receiver


receivers=['christopheremanuel97@gmail.com', 'nadine.salem@ttu.edu', 'joshuwes@ttu.edu', 'pedro.arredondo@ttu.edu'  ]


for i in range(len(receivers)):
    for j in range(15):
        smtp.sendmail('jcala0509@gmail.com',receivers[i], msg.as_string())
smtp.quit() #dont forget to clear connection