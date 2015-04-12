# Send those sms
import requests



def sendSMS(num, content):
    headers = {'User-Agent':'LOL'}
    url = 'http://textbelt.com/text'
    payload = {"number":num, "message":content}
    m = requests.post(url, data=payload, headers=headers)
    print(m.text)
    print()
    print(payload)

sendSMS(7042925045, 'I wanted to test if the connection to the server is encryptable. Please let me know if you get this. It will be the last one today')

"""
def send_text(numstring, message):
    message = {"number": numstring, "message": message}
    r = requests.post("http://textbelt.com/text", data=message)
    print(r.status_code)
    print()
    print(r.text)
    return r.status_code, r.text
"""

