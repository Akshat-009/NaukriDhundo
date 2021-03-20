import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random 
import string 

def send_mail(receiver, subject, message):

    me = "ENTER_YOUR_EMAIL"
    my_password = "YOUR_PASSWORD"
    you = receiver

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you

    html = message
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('mail.privateemail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

def rand_str(n=25):
    return "".join([random.choice(string.ascii_letters) for s in range(n)])