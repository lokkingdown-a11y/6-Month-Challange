person = {}
person['Name'] = 'Rahim'
print(person)

person = {
    'name' : 'Antu'
}
find = input('Enter Nam Key: ')
result = person.get(find)
if find is None:
    print(f'{find} not found')
else:
    print(f'{find} is available')
    print(f'This is Your Value {result}')



if find != person:
    print(f'{find} Not Found')
else:
    print(f'{find} thst is result')


list_c = [x for x in range(1,31) if x % 5 == 0]
print(list_c)


dictofn = {x:x**2 for x in range(1,6)}
print(dictofn)

def multipy(a,b = 2):
    return a * b
    
rsult = multipy(5)
print(rsult)



def list_function():
    defaul =[]
    for i in range(5):
        lst = int(input('Enter NUmber: '))
        defaul.append(lst**2)
    return defaul

result = list_function()
print(result)

lst_c = {x:x**3 for x in range(1,6)}
print(lst_c)

with open('test.txt','w') as f:
    lines = f.write('Make a game using html' \
    'a man who play game regularly he is always felt very happy ' \
    'and healthy')
    print(lines)

with open('download.jpg','rb') as f:
    f.read()

ফাইল না থাকলে auto-create হবে
with open('new_file.txt', 'w', encoding='utf-8') as f:
    print(f.write('এই লেখার সাথে সাথে ফাইল তৈরি হয়ে গেল!'))

with open('New File.py','w',encoding='utf-8') as f:
    print(f.write('name = Antu '))
import json
bio_data = {
    "name" : "Antu",
    "age" : 20,
    "profession" : "Nothing",
    "Adress" : {"Adress1" : "Jashore",
                "adress2" : "Churamonkati",
                "Parmanent Adress": "Nothing"
                },
    "status" : "Student"

}
with open('bio_data.json','w', encoding='utf-8') as f:
    json.dump(bio_data, f, indent=4, ensure_ascii=True)
print('Succesfully Created')

with open('test.txt','w',encoding='utf8') as f:
    print(f.write('Hi How Are You? '))

import json 
data = {"brand": "Toyota", "price": 500}
with open('data.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4)
print('Succesfully Created')
import json
with open('data.json','r',encoding='utf-8') as f:
    dt = json.load(f)


    name = dt.get("NAme")
print(f'This Is Your data  {name}')
একটি খালি ক্লাস তৈরি করুন

