import requests
from PIL import Image
img = Image.open("python/images.png")
CHAT_ID = "7555634162"
TOKEN = "8906882422:AAHHopv0cXz2oQcORvs3zG--Xc4-WliWn0I"
url =  f"https://api.telegram.org/bot{TOKEN}/sendMessage"

body = {
    "chat_id" : CHAT_ID,
    "file" : img
}

response = requests.post(url,json=body)
nm = response.json()
print(nm)

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# script নিজে যে ফোল্ডারে আছে, সেটা থেকে path বানানো (আগে যেভাবে শিখেছিলে)
script_folder = Path(__file__).parent
FILE_PATH = script_folder / "python" / "images.png"

url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

payload = {
    "chat_id": CHAT_ID,
    "caption": "Your File"
}

if not FILE_PATH.exists():
    print(f"ফাইল পাওয়া যায়নি: {FILE_PATH}")
else:
    with open(FILE_PATH, "rb") as file:
        files = {"document": file}
        response = requests.post(url, data=payload, files=files)
    print(response.json())


nak = {
    "Name" : "Antu",
    "age" :   23,
    "status" :"Student"
}

for key,value in nak.items():
    print(F"Key = {key},          Value = {value}")

tup = (2,3,45,2,1)
print(tup[2])

fruits = {
    "fruit1" : "apple",
    "fruit2" : "mango",
    "fruit3" : "orange",
    "fruit4" : "jackfruit"
}

for m,n in fruits.items():
    print(f"key = {m} Value = {n}")


def word_counter(sentence):
    na = sentence.split()
    counts = {}
    for name in na:
        for i in len(na):
            counts[f"word{i}"] = name
    print(counts)

word_counter("My name is Antu AR")


import os
from dotenv import load_dotenv
load_dotenv()
to = os.environ.get("mo")
print(to)

class exp_trc():
    def __init__(self,month,income,expend):
        self.month = month
        self.income = income
        self.expend = expend
    def cal(self):
        inc = self.income
        exp = self.expend
        total = inc - exp
        print(total)
    def summerry(self):
        return {
            "month" : self.month,
            "income" : self.income,
            "expend" : self.expend,
            "Balance" : self.cal()
        }

b_dic = []
b_dic.append(exp_trc(1,2000,30))
b_dic.append(exp_trc(2,3500,60))
print(b_dic)
for r in b_dic:
    print(r.summerry())


# #Task 1
# marks = {"Antu": 85, "Rafi": 92, "Sadia": 78}
# max = marks["Antu"]
# for i,m in marks.items():
#     if max < m:
#         max = m
#     else:
#         max = max

# print(max)

#Task 2
# def calc(a,op,b):
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     elif op == "/":
#         return a /b
#     else:
#         return "System Error"
    
    

# def call():
#     con = input("Can You want to Continue(y/n): ")
#     while True:
#         if con.lower() == "y":
#             result = calc(int(input("enter Number: ")),input("Enter Operator: "),int(input("Enter Number: ")))
#             print(result)
#             break
#         if con.lower() == "n":
#             break
# while True:
#     call()  

#Task 3
# class bankac():
#     def __init__(self,holder_name,balance):
#         self.holder_name = holder_name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount

#     def list_of_user(self):
#         list = []
#         list.append({
#             "name" : self.holder_name,
#             "Bank Balance" : self.balance
#         })
#         for i in list:
#             print(i)

# user1 = bankac("Antu",2000)
# user1.deposit(5000)
# user1.list_of_user()

#Task4
# import os
# file = os.listdir("Web_Development")
# list = []
# for i in file:
#     list.append({
#         "File" : i
#     })
# print(list)
# if os.path.exists(".html"):
#     newlist = []
#     newlist.append({
#         "Path" : os.path.exists(".html")
#     })
#     print(newlist)

#Task 5

try:
    num = int(input("Your Number: "))
    crcnum = 25454
    def nums():
        if num != crcnum:
            print(f"Please Enter Correct Number This Number {num} is invalid")
    while num != crcnum:
        nums()
        if num == crcnum:
            break


except ValueError:
    print("Please Enter Only Number")
    nums()

Task 1
name = "Antu" 
age = 18
print(f"Welcome How Are You  {name} ? and Your Age {age} semms like you are adult")
Task2
for i in range(1,11):
    print(i)
Task3
total = 0
for i in range(2,102):
    total += i
print(total)
Task4
c_list = ["Free Fire", "Python", "AI"]
for i in c_list:
    print(f"I Love {i}")
Task5
num = int(input("Enter Number: "))
if num % 2 == 0:
    print(f"The Number {num} is Even")
else:
    print(f"The Number {num} id Odd")
Task6
i = 6
while i > 1:
    i -= 1
    print(i)
Task7
strin = input("Enter Sentence: ")
print(len(strin))
Task8
list = [2,5,6,4,8]
max = list[0]
for i in list:
    if max < i:
        max = i
    else:
        max = max

print(max)

Task9
for i in range(1,6):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

Task 10
string = input("Enter Sentence: ")
data = string[::-1]
print(data)

Task 11
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
new = is_even(5)
print(new)

Task 12
def num():
    list = []
    for i in range(1,4):
        i = input("Enter Number: ")
        list.append(i)
    print(list)
    max = list[0]
    for j in list:
        if max < j:
            max = j
        else:
            max = max
    print(max)
num()

Task13
dict = {"Antu": 1200,
         "Rafi": 800}
for k,v in dict.items():
    if v > 1000:
        print(f"The Maximum number of Name Is {k}")
    
Task14
sent = input("Enter Sentence: ")
n = sent.split()
print(len(n))

Task15
total = 0
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        total += i

print(total)
        
Task 16
def cheker():
    num_list = []
    n = int(input("how many number you want to input: "))
    total = 0
    for i in range(1,n):
        num = int(input("Enter Number: "))
        num_list.append(num)
    for j in num_list:
        total += j
    kj = total / len(num_list)
    print(kj)
cheker()
Task17
word = input("Enter Word: ")
ulta = word[::-1]
if word == ulta:
    print("The Word Is Palindrome")
else:
    print("The Word IS Not PalinDrome")

Task18
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        list = []
        list.append(name)
        list.append(marks)
        if marks > 80:
            print(name)
        
Studeng = Student("Antu",90)
studemt = Student("Chondon",67)
studengd = Student("Dipto",81)
Task19
charac = str(input("Enter Your Word or symbol: "))
for i in range(1,6):
    design = charac*i
    print(design)    
Task20
import asyncio
async def task():
    print("Task1 started.........")
    await asyncio.sleep(0.5)
    print("Task1 Complited.........")
async def task1():
    print("Task2 started.........")
    await asyncio.sleep(4)
    print("Task2 Complited.........")
async def task2():
    print("Task3 started.........")
    await asyncio.sleep(3)
    print("Task3 Complited.........")
async def task3():
    print("Task4 started.........")
    await asyncio.sleep(6)
    print("Task4 Complited.........")
async def main():
    await asyncio.gather(task(),task1(),task2(),task3())

asyncio.run(main())

import asyncio
async def downlo():
    print("Starting Download.................")
    asyncio.sleep(6)
    print("Download Succesfully")
    return "file.pdf"
async def main():
    task = asyncio.create_task(downlo())
    print("Downloading I am doing now another work........")
    await asyncio.sleep(2)
    print("I am Work More....")
    result = await task
    print(f"The Result Is {result}")
asyncio.run(main())


import asyncio
async def hel():
    print("Task1........")

asyncio.run(hel())

import asyncio
async def task1():
    print("Task1 Start Now...........")
    await asyncio.sleep(3)
    print("Completed Task 1")
async def task2():
    print("Task2 Start Now...........")
    await asyncio.sleep(3)
    print("Completed Task 2")
async def task3():
    print("Task3 Start Now...........")
    await asyncio.sleep(3)
    print("Completed Task 3")

async def main():
    await asyncio.gather(task1(),task2(),task3())

asyncio.run(main())


import asyncio

async def down():
    print("I am start now Downloading.............")
    await asyncio.sleep(4)
    print("Your File Downloaded.")
    return "bot.py"
async def man():
    task = asyncio.create_task(down())
    print("I am Doing Now Another Task")
    await task
    print("all is Done")
asyncio.run(man())

import asyncio
async def work():
    print("The Work Is Starting Now......!")
    await asyncio.sleep(6)
    print("Work Is Done")
    return "Task Is Completed"
async def main():
    try:
        result = await asyncio.wait_for(work(),timeout=7)
        print(f"The  Work {result}")
    except TimeoutError:
        print("sorry prgram has been timeout error")

asyncio.run(main())

import requests
import asyncio
async def provider1():
    try:
        API = "fksjafhsnkahdfedjajfaapi"
        url = "example.com"
        header = {
        "User-Agent" : "my-name-1.0"
        }
        await asyncio.sleep(5)
        output = requests.get(url,API,headers=header)
        print(output)
    except KeyError:
        print("check Your api")
    except ConnectionError:
        print("Check Your Connection")
    except TimeoutError:
        print("Connection Timeout Trying Next..........")
async def provider2():
    user = input("enter message: ")
    replay = "How can i assist Today"
    print(user)
    await asyncio.sleep(3)
    print(replay)

async def main():
    try:
        await asyncio.wait_for(provider1(),timeout=9)
    except asyncio.TimeoutError:
        print("Program Timedout.....")
        await provider2()

asyncio.run(main())


import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = "https://api.mistral.ai/v1/chat/completions"
header = {
    "Authorization" : f"Bearer {os.getenv('MISTRAL_API_KEY')}",
    "Content-Type" : "application/json"
}
body = {
    "model" : "mistral-small-latest",
    "messages" : [
        {
          "role" : "user",
          "content" : input("Enter Message: ")
        }
    ]
}

resp = requests.post(url,headers=header,json=body,timeout=20)
m = resp.json()
print(m)


import asyncio
async def main():
    que = asyncio.Queue("MY Name")
    print(que)
asyncio.run(main())

import asyncio
async def main():
    que = asyncio.Queue()
    na = que.put("Name")
    print("Puting........")
asyncio.run(main())



import asyncio
async def main():
    que = asyncio.Queue()
    await que.put("My name is Antu AR,The Ceo OF AR Company")

    fort =  await que.get()
    print(f"The Item is This {fort}")

asyncio.run(main())


import asyncio
async def producer(que):
    for i in range(1,9):
        print(f"Loaded: {i}")
        await asyncio.sleep(2)
        await que.put(i)
async def getters(que):
    for i in range(1,9):
        print(f"Loading.......")
        await asyncio.sleep(1)
        na = await que.get()
        print(f"Processing: {na}.")
async def main():
    que = asyncio.Queue()
    await asyncio.gather(producer(que),getters(que))

asyncio.run(main())
