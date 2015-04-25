# Send those sms
import requests

def sendSMS(num, content):
    headers = {'User-Agent':'LOL'}
    url = 'http://textbelt.com/text'
    payload = {"number": num, "message": content}
    m = requests.post(url, data=payload, headers=headers)
    print(m.text)
    print()
    print(payload)

sendSMS(7045552222, 'This is my message')
