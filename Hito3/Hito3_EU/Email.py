import requests
import json

def GenerteRandomEmail():
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    response = requests.get(url)
    data = json.loads(response.text)
    result = data[0]
    #print(data)
    return result

def EmailList(mail):
    user= mail.split('@')[0]
    domain = mail.split('@')[1]
    #print(user)
    #print(domain)
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}"
    response = requests.get(url)
    result = json.loads(response.text)
    return result

def ReadEMail(mail,id):
    user = mail.split('@')[0]
    domain = mail.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={id}"
    response = requests.get(url)
    result = json.loads(response.text)
    return result
