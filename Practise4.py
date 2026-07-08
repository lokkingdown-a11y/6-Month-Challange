phonebook = {}
phonebook['Name'] = 'Antu'
phonebook['Name1'] = 'Chondon'
phonebook['Name2'] = 'joy'
phonebook['Name3'] = 'Dipto'
phonebook['Name4'] = 'Opu'
phonebook['Name5'] = 'Sadhin'
phonebook['Name6'] = 'Choyon'
phonebook['Name7'] = 'Tanjim'
phonebook['Name8'] = 'Rik'
phonebook['Name9'] = 'Biplob'
phonebook['Name10'] = 'Ciam'
phonebook['Name11'] = 'Jisan'
phonebook['Name12'] = 'Jisan'
phonebook['Name13'] = 'Abdullah'
phonebook['Name14'] = 'Nirob'
print(phonebook)
list = {
    'name' : 'antu',
    'Number' : 1328112327,
    'age' : 23
}
list['name'] = 'Opu'
print(list)
name = {
    'name' :    []
}
for i in range(1,4):
    name['name'].append(input('Enter Name: '))
print(name)
phonebook = {'Name' : ['Antu']}
for i in range(1,4):
    phonebook['Name'].append(input('Enter Name: '))
print(phonebook)
if name in phonebook:
    phonebook['Name'].append(name)
    phonebook['Age'].append(age)
else:
    phonebook['Name'] = [name]
    phonebook['Age'] = [age]

print(phonebook)


phonebook = {'Name':[],
             'Age' :[]  }
name = input('Enter Name: ')
age = int(input('Enter Age: '))
phonebook['Name'] = [name]
phonebook['Age'] = [age]
while True:
    c_j = input('Can You Want To Continue(y/n): ')
    if c_j == 'y':
        phonebook['Name'].append(input('Enter Name: '))
        phonebook['Age'].append(input('Enter Age: '))
    else:
        print('Program Ended')
        break
print(phonebook)

import json
with open('student_data.json') as file:
    loaded_data = json.load(file)
print(loaded_data)
print(loaded_data['name'])
try: 
    json.load(f)
except FileNotFoundError: 
    print("ফাইল নেই")


list_n = [2,5,2,4,6,7,3,2,7]
result = sum(list_n)
print(result)

num = int(input('Enter Number: '))
if num % 2 == 0:
    print('The Number Is Even')
else:
    print('The Number Is Odd')

list_num = []
for i in range(1,4):
    num = int(input('Enter Num: '))
    list_num.append(num)
if list_num[0] > list_num[1]:
    print(list_num[0], 'Is A Big Number')
elif list_num[1] > list_num[0]:
    print(list_num[1],'is a Big Number')
elif list_num[2] > list_num[1]:
    print(num[2],'Is Big Number')
elif list_num[0] > list_num[2]:
    print(list_num[0],'IS Big Number')
elif list_num[2] > list_num[0]:
    print(list_num[2],'Is A Big Number')
else:
    print('Error')

for i in range(1,21):
    if i % 4 == 0:
        continue
    print(i)

list_of_num = [5, 10, 15, 20]
list_of_num.append(25)
print(list_of_num)

listn = [10, 20, 30]
last_e = listn.pop()
print(last_e)
list_n = []
for i in range(5):
    num = int(input('Enter Number: '))
    list_n.append(num)
print(list_n)

total = 0
number = [2,5,6,8,6,3,7,4,5]
for num in number:
    total = total + num
print(total)


numbers = [5, 1, 9, 3]
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num


print(max_num)


dict_p = {}
dict_p['Name'] = 'Rahim'
dict_p['Age'] = 23
print(dict_p)

