# Send those sms
import requests 
url = 'http://textbelt.com/text' 
def sendSMS(num, content):
    number = None
    message= None

    stringNum = str(num)
    payload = {}
    payload[number]=stringNum
    payload[message]=content
    m = requests.post(url, data=payload)
sendSMS(7042925045, 'Hello Alex')
