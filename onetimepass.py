import math
import random
import smtplib
import os


def otp_function(email):
    
    digit = "0123456789"
    otp = ""
    for i in range(4):
        z=math.floor(random.random() * 10)
        otp = otp + digit[z]
    print(otp)

    subject = "OTP verification for HMS"
    body = f"Hi, Your OTP is: {otp}"
    msg = f"Subject: {subject}\n\n{body}"
    #host name
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.ehlo() 
    Email_id = os.environ.get('email')
    password = os.environ.get('password')
    s.login(Email_id, password)
    send_to = email

    s.sendmail(Email_id, send_to, msg)
    print("OTP sent successfully.")

    return otp

def verify(otp1,otp2):
    if otp1 == otp2:
        print("Success")
        return 1
    else:
        return 0
    return 0
