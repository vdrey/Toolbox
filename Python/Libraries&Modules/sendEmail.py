# This uses Email Yak to send an email
 
import requests
import json
import os

def sendEmail(API_KEY=None, To=None, From=None, CC=None, BCC=None, Subject=None, Message=None):
    # Still need to add all Email Yak fields
    url = 'https://api.emailyak.com/v1/' + API_KEY + '/json/send/email/'
    
    headers = {'Content-Type' : 'application/json'} # This is still needed. 
                                                    #Possibly need to account for http vs email headers
    sendFrom = "1027@ohos.simpleyak.com"
    content = {"FromAddress": sendFrom, "ToAddress": email,
               "Subject": "1027 Patricians Lane IP Address Change",
               "TextBody": message} # Make this so that it is standardized
    JSONcontent = json.dumps(content)
    sendMail = requests.post(url, data=JSONcontent, headers=headers)
    print(sendMail.json())
