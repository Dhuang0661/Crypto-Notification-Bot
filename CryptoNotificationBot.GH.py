import requests
import json
import smtplib
from email.message import EmailMessage
import time

#The API I used is from Coinbase
coinBaseAPI='https://api.coinbase.com/v2/prices/'
name=input("Enter the ticker of the coin:")

#This function request data from the Coinbase API
def cryptoPrice(crypto):
    global data
    response=requests.get(coinBaseAPI+crypto+'-USD/spot')
    data=response.json()
    print (data)
    return data
    
#This function sends messages. In this case, this function send the data retrieved 
#from the API
def SMSNotification(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to

    user="#SenderEmailAddress"
    password="#Password"
    msg['from']=user

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    
    server.quit()


#You need to find the MMS Gateway Domain for specific carrier
#https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/
while True:
    cryptoPrice(name)
    SMSNotification("Coin Alert",str(data),"#MMSGatewayDomain")
    time.sleep(300)