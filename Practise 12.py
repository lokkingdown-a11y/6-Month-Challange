import requests
import json
url = 'https://randomuser.me/api/'

header = {
    "User-Agent" : "my-app-1.0"
}
data = requests.get(url,headers=header,timeout=40)

json_former = data.json()

m_data = json.dumps(json_former,indent=4)

print(m_data)
print(data.status_code)


import requests
import json

url = "https://api.mistral.ai/v1/chat/completions"

API = "czDo6RC9WH25sWyci9qbRaizWrdJw4yh"
header = {
    "Authorization" : f"Bearer {API}",
    "Content-Type" : "application/json"
}

body = {
    "model" : "mistral-small-latest",
    "messages" : [
        {
            "role" : "user",
            "content" : input('Enter Messege: ')
        }
    ]
}

main_request = requests.post(headers=header,url=url,json=body)
n = main_request.json()
jsonf = json.dumps(n,indent=4)
m = n["choices"][0][ "message"]["content"]
print(m)


import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv()
API = os.getenv("api")

url = "https://api.mistral.ai/v1/chat/completions"

header = {
    "Authorization" : f"Bearer {API}",
    "Content-Type" : "application/json"
}

body = {
    "model" : "mistral-small-latest",
    "messages" : [
        {
            "role" : "user",
            "content" : input("Enter Your Messege: ")
        }
    ]
}

try:
    data =requests.post(url=url,headers=header,json=body,timeout=40)
    resp = data.json()
    n = json.dumps(resp,indent=4)
    m = resp["choices"][0][ "message"]["content"]
    print(m)
    print(data.status_code)

except KeyError:
    print("Maybe Your Api Is Not Correct")
    print("Check It Again")

except ConnectionError:
    print("Maybe Your Intenet Has Gone")
    print("ensure Internet Connection")

except requests.exceptions.ConnectionError:
    print('Please Check Internet Connection')


import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API = os.getenv("api")

url = "https://api.mistral.ai/v1/chat/completions"

header = {
    "Authorization" : f"Bearer {API}",
    "Content-Type" : "application/json"
}


cpnv = []

while True:
    u_i = input("Enter Message: ")
    if u_i.lower() == "exit":
        break
    

    cpnv.append({"role" : "user","content" : u_i})
    
    data = {
    "model" : "mistral-small-latest",
    "messages" : cpnv
}
    try: 
       n = requests.post(url=url,headers=header,json=data,timeout=10)
       m = n.json()
       me = m["choices"][0][ "message"]["content"]
       print(f"AI: {me}")
    except KeyError:
        print("wait")


    

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

API = os.getenv('api')

header = {
    "x-goog-api-key" : API,
    "Content-Type" : "application/json"
}

body = {
    "contents": [
        {
            "parts": [
                {"text": input("Enter Message: ")}
            ]
        }
    ]
}

resp = requests.post(url=url,headers=header,json=body,timeout=400)
msg = resp.json()
n = json.dumps(msg,indent=4)
m_me = msg["candidates"][0]["content"]["parts"][0]["text"]
print(m_me)


ner_dic = {
    "name" : "Antu",
    "AIM"  : {
        "first-aim" : "AI MHB",
        "second-aim" : {
            "aim" : "make-the-world-for-god",
            "aim2nd" : [{
                "aim3" : "make the ai who copy him"
                 
                }
            ]
        } 
    }
}


name = ner_dic["AIM"]["second-aim"]["aim2nd"][0]
print(name)


student = {
    "name": "Antu",
    "subjects": ["Python", "Automation", "Web"],
    "info": {
        "age": 20,
        "city": "Khulna"
    }
}


data = student["info"]["city"]
print(data)


num = [2,5,9,6,7]
n = float(input("Enter Number: "))
if n in num:
    print("available")
else:
    print("not available")


একটা fake API response বানাও নিজে, তারপর বের করার practice করো
fake_response = {
    "status": "success",
    "users": ["Antu", "Rahim", "Karim"],
    "settings": {
        "auto_reply": True,
        "language": "bn"
    }
}

এখন নিজে বের করো:
১. status কী সেটা
২. users লিস্টের দ্বিতীয় জন কে
৩. auto_reply চালু আছে কিনা

status = fake_response["status"]
users2nd = fake_response["users"][1]
print(status)
print(users2nd)

if fake_response["settings"]["auto_reply"] == True:
    print("auto replay on")
else:
    print("auto replay off")


def name(exp):
    print(f"welcome {exp}")
name("Antu")


def get_replay(name,model = "mistral-small-latest"):
    print(f"The Name Of AI Is This {name}")
    print(f"The Name Of model is {model} ")

get_replay("Mistral")

def num_verify(n):
    seq = n*n
    if seq % 2 == 0:
        ty = "even"
    else:
        ty = "odd"

    return seq,ty

a,b = num_verify(6)
print(a)
print(b)

def num(*numers):
    l = sum(numers)
    return l

nums = num(5,8,9,2,5,6,3,8,6,5,7)
print(nums)

import json
def value(**details):
    print(details)

n = value(name = "Antu" , Age = 22 , ocuupation = "nothing")
m = json.dumps(n,indent=4)

print(m)


Task1 Easy Task
def data(name):
    print(f" Welcome {name}")

data("Antu")

Task 2 Easy Task
def task2(num,exp = 2):
    return num ** exp

n = task2(4)
print(n)

Task 3 Medium
def divide(a,b):
    try: 
        if a % b == 0:
            return True
        else:
            return False
    except ZeroDivisionError:
        print(None)

num = divide(5,0)
print(num)

Task 4 Medium Task
def check_number(num):
    if num % 2 == 0:
        mode = f"The Number {num} is even"
    else:
        mode = f"The Number {num} is odd"

    print(mode)
check_number(89)

Task 5 Medium Hard
def sumn(*number):
    print(sum(number))
    averege = sum(number) / len(number)
    print(averege)
sumn(5,9,2,5,2,6,5,3,7,9,85,5)


Task 6 Hard 
def user_profile(**details): 
    print(details.get("name"))
    print(details.get("Age"))

user_profile(name = "Antu",Age = 23,status = "Nothing")

Task 7 Hard
def ns(*nums,**settings):
    n = sum(nums)
    if "multiply" in settings:
        return n * settings["multiply"]
    else:
        return n
    
lok = ns(5,9,6,78,3,6,4,multiply = 3)
print(lok)

Task 8 Very Hard
def api_call_sim(message, model="mistral-small"):
    fake = {"choices": [{"message": {"content": "AI er reply"}}]}
    reply_text = message
    try:
        if reply_text in fake:
            return reply_text,True
        else:
            return None,False
    except KeyError:
        print("none")

l = api_call_sim("AI er reply")
print(l)


Task 9 Ultra Hard
def bot_handler(*messages, **config):

with open("note.text",'w') as f:
    n = f.write("My First Notes")
   
# with open("note.text",'r') as k:
#     m = k.read()
#     print(m)

with open("note.text",'a') as t:
    o = t.writelines("\n i am a boy")

with open("note.text",'r') as q:
    y = q.readlines()
    print(y)


import json
data = {
    "name" : "Antu",
    "age" : 23,
    "city" : "Jashore"
}

with open("data.json","w") as f:
    mn = json.dump(data,f,indent=4)

with open("data.json","r") as fl:
    mn = json.load(fl)
    print(mn)
    
a = float(input("Enter Number: "))
b = float(input("Enter Number: "))
try:
    division = a/b
    print(division)
except ZeroDivisionError:
    print("Please Enter The Number Not 0")
finally:
    print("Not Forget That The Division Of 0 is Always Return Error")
