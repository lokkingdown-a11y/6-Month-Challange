import requests
url = 'https://deepseek.com/'
response = requests.get(url)
print('\n---------Your data---------')
print(response.text)

import requests
url = 'https://openweathermap.org/'
resp = requests.get(url)
data = resp.json()

print('\n-----------------Your Json Data-----------------')
print(data)
print('My Present Data',data['headers']['User Agent'])

import requests
url = 'https://api.ipify.org?format=json'
resp = requests.get(url,params={'ip':''})
print('\n-------------Your Datas-------------')
print(resp.text)

import requests
header = {"User-Agent": "MySchoolProject/1.0"}
url = 'https://httpbin.org/get'
resp = requests.get(url,headers=header)
data = resp.json()
my_agent = data["headers"]["User-Agent"]
print('\n-------------------Your Data-------------------')
print(my_agent)
import requests
url = 'https://api.github.com/users/octocat'
header = {
    "User-Agent": "যে কোন নাম",
    "Accept": "application/vnd.github.v3+json"
}
resp = requests.get(url,headers=header)
data = resp.json()
my_data = data["public_repos"]
my_data1 = data["name"]
my_data2 = data["login"]
print('\n-----------------------Your Data---------------------------')
print(my_data)
print(my_data1)
print(my_data2)

import requests
API_KEY = '3aeea700f8bf0d21d1c3eeb818f1794d'
city = 'Dhaka'

params = {
    'q' : city,
    'appid' : API_KEY,
    'units' : 'metric'
}

headers = {
    'User-Agent' : 'WeatherApp/1.0'
}

url = 'https://api.openweathermap.org/data/2.5/weather'

try:
    resp = requests.get(url,headers=headers,params=params,timeout=10)
    resp.raise_for_status()
    data = resp.json()
    temprature = data['main']['temp']
    description = data["weather"][0]["description"]

    print(f"City: {city}")
    print(f"Temprature: {temprature}°C")
    print(f"Sky: {description}")


except requests.exceptions.RequestException:
    print('HTTP Error Try Again')

except KeyError:
    print('Check Your API Keys')


import requests
from urllib.parse import urlparse,parse_qs
eurl = 'https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=REAL_KEY&units=metric'
parsed = urlparse(eurl)
parmas_as_dict = parse_qs(parsed.query)
params = {k: v[0] for k, v in parmas_as_dict.items()}
print(f'The Params Dictionary', params)
resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
# print(resp.json()['main']['temp'])
print(f'Your Code is ',resp.status_code)



import requests
import json
url = 'https://randomuser.me/api/'
header = {
    'User-Agent' : 'app.myproject'
}
resp = requests.get(url,headers=header,timeout=10)
data = resp.json()
# print(data)

try:
    first_name = data["results"][0]["name"]["first"]
    last_name = data["results"][0]["name"]["last"]
    print(first_name + last_name)
except requests.exceptions.RequestException:
    print('Http Server Error')
except KeyError:
    print('Check Full Code Again')

import requests
url = 'https://randomuser.me/api/'
header = {
    "User-Agent" : "My-Project.BD"
}
resp = requests.get(url,headers=header,timeout=10)

try:
    data = resp.json()
    first_name =  data.get("results", [{}])[0].get("name", {}).get("first")
    print(first_name)
except KeyError:
    print("Chek Your Code Again")


import requests
import json
url = 'https://randomuser.me/api/'
header = {
    "User-Agent" : "My-Project/1.0"
} 
resp = requests.get(url,headers=header,timeout=10)

try:
    data = resp.json()
    print(json.dumps(data,indent=4))
    # name = data.get("results", [{}][0].get("name", {})).get("first")
    name = name = data.get("results", [{}])[0].get("name", {}).get("first")
    print(name)

except KeyError:
    print("Chek The Code Again")



import requests
import json
url = 'https://api.mistral.ai/v1/chat/completions'
API_KEY = 'gY5QUgH7oB15xorZVJFQDORILRhSa0X5'
headers = {
    "Authorization": f"Bearer {'gY5QUgH7oB15xorZVJFQDORILRhSa0X5'}",
    "Content-Type": "application/json"
}
body = {
    "model" : "mistral-small-latest",
    "messages" : [
        {
            "role" : "user","content" : input('Enter Messege: ')
        }
    ],
    "temperature" : 0.7
}
resp = requests.post(url, headers=headers,json=body,timeout=30)
print(resp.json())
print(resp.status_code)
try:
    data = resp.json()
    jsondata = json.dumps(data,indent=4)
    print(jsondata)

except KeyError:
    print("Check Code Again")


import requests
import json

def data():
    url = 'https://api.mistral.ai/v1/chat/completions'
    API_KEY = 'gY5QUgH7oB15xorZVJFQDORILRhSa0X5'

    headers = {
        "Authorization" : f"Bearer {API_KEY}"
    }

    body = {
        "model" : "mistral-small-latest",
        "messages" : [
            { 
                "role" : "user" , "content" : input('Enter Messege: ')
            }
        ],
        "temperature" : 0.7
    }

    output = requests.post(url,headers=headers,json=body,timeout=10)

    try:
        resp = output.json()
        data = json.dumps(resp,indent=4)
        print(data)
    except KeyError:
        print('Check Your Api or py code')

i = 1
while i < 1000*10000:
    data()
    i+=1


import requests as o
import json
url = "https://randomuser.me/api/"
resp = o.get(url)
data = resp.json()
json_data = json.dumps(data,indent=4)
# print(json_data)

first = data["results"][0]["name"]["first"]
location = data["results"][0]["location"]["street"]["number"]
print(first)
print(location)


import requests
import json
url = "https://api.github.com/repos/lokkingdown-a11y/6-Month-Challange"
resp = requests.get(url)
full_data = resp.json()
data = json.dumps(full_data,indent=4)
login = full_data["owner"]["login"]
print(data)
print(login)

import requests
import json
url = "https://api.openweathermap.org/data/2.5/weather"

API_KEY = "3aeea700f8bf0d21d1c3eeb818f1794d"
headers = {
    "User-Agent" : "my-app-1.0"
}


params = {
    "q" : input("Enter Your City: "),
    "appid" : API_KEY,
    "units" : "metric"
}

resp = requests.get(url,headers=headers,params=params,timeout=10)

try:
    data = resp.json()
    # print(json.dumps(data,indent=4))
    name = data["weather"][0]["main"]
    temprature = data["main"]["temp"]
    print(f"The Temreture Of {params['q']} is This {temprature}")
    print(f"The Data Is This {name}")
except requests.RequestException:
    print("Check Code again")
except KeyError:
    print("Check Again")


import requests
import json
import pandas as pd

url = "https://randomuser.me/api/"

header = {
    "User-Agent" : "My-app-3.5"
}

resp = requests.get(url,headers=header,timeout=10)
data = resp.json()
json_data = json.dumps(data,indent=4)

first = data["results"][0]["name"]["first"]
last = data["results"][0]["name"]["last"]
email = data["results"][0]["email"]
country = data["results"][0]["location"]["country"]
username = data["results"][0]["login"]["username"]


data_csv ={
    "name" : [first + last,first + last,first + last,first + last],
    "email" : [email,email,email,email],
    "Country" : [country,country,country,country,],
    "Username" : [username,username,username,username,]
}

main_data = pd.DataFrame(data_csv)
print(main_data)

import requests
import json
import pandas as pd

url = "https://randomuser.me/api/"

header = {
    "User-Agent" : "My app-4.8"
}

resp = requests.get(url,headers=header,timeout=10)

data = resp.json()

main_data = json.dumps(data,indent=4)

first = data["results"][0]["name"]["first"]
last = data["results"][0]["name"]["last"]
email = data["results"][0]["email"]
country = data["results"][0]["location"]["country"]
username = data["results"][0]["login"]["username"]

data1 = {
    "name" : first + last,
    "email" : email,
    "country" : country,
    "Username" : username
}

with open('data1.json','w') as f:
    mf = json.dump(data1,f,indent=4)
    print(mf)

print(json.dumps(data1,indent=4))
