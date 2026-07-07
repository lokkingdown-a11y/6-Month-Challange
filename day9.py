bdt = float(input('Enter BDT: '))
print(f'Your USDT IS {bdt * 0.0079365079365079}')
usd = float(input('Enter USDT: '))
print(f'Your BDT Is {usd*126}')

c_r_pass = 'antu009'
def passwn():
    usr_pss = input('Enter Password: ')
    if usr_pss == c_r_pass:
        print(f'Your Password {usr_pss} is correct')
        return True
    else:
        print('Try Again')
while True:
    if passwn():
        break

n = int(input('Enter Num: '))
total = 0 
for i in range(1,n+1):
    total += i

print(total)
import pandas as pd
data = {
    'Name' : ['Antu','Chondon','Dipto','Opu','Nirob','Joy'],
    'Age' : [20,23,24,19,17,25],
    'Sallary' : [20000,23000,25000,35000,15000,23000],
    'Medical Salary' : [2300,2300,2300,2300,2300,2300]
}

df = pd.DataFrame(data)
df['Tax'] = df['Sallary'] * 0.05
df['House_Rent'] = df['Sallary'] * 0.05
df['Total'] = df['Sallary'] + df['Medical Salary'] - df['Tax'] + df['House_Rent']
print(df)

for i in range(1,2):
    n = f'file{i}.py'
    with open(n,'w') as f:
        new = f.write('Antu')
print(new)

import json
data = {
    "name" : "Antu",
    "age" : 23,
    "status" : "Student"
}
with open('Ar.json','w') as f:
    final = json.dump(data,f,indent=4)
class storage:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'Your name is {self.name} and age is {self.age}')

name1 = storage('Antu',22)
name2 = storage('Opu',23)
name3 = storage('Dipto',24)
name4 = storage('Joy',12)
name5 = storage('Choyon',23)
name6 = storage('Nirob',24)
name1.show()
name2.show()
name3.show()
name4.show()
name5.show()
name6.show()

import pandas as pd
data = {
    'name' : ['Antu','Chondon','Dipto','Joy','Nirob'],
    'age' : [23,24,25,22,21],
    'Status' : ['Student','Student','Student','Student','Student']
}
df = pd.DataFrame(data)
df['year'] = 2026 - df['age']
# df['aqurate_date'] = pd.to_datetime(df['year'])
# duplidata = df.drop_duplicates(subset=['Status'])
# print(f'Your Data Is {df[['name','age']]}')
# print(duplidata)
def age_ctgr(age):
    if age < 22:
        return 'child'
    elif age < 23:
        return 'mid-age'
    else:
        return 'Adult'
    
df['Afe_ctr'] = df['age'].apply(age_ctgr)
        
print(df)

import pandas as pd
data = {
    'name' : ['Antu','Chondon','Dipto','Joy','Nirob'],
    'age' : [23,24,25,22,21],
    'Status' : ['Student','Student','Student','Student','Student']
}
df = pd.DataFrame(data)
  
