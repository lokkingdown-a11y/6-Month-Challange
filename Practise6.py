import json
data = {
    "NAME": "Antu",
    "AGE" : 23,
    "company" : {
        "1st Company" : "Mototus",
        "2nd Company" : "Noraton"
    }
}
with open('data.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4)
    print('SUCCESFULLY Created')

class student:
    def __init__(self,name,id,gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

    def show_infp(self):
        print(f'The Student Name {self.name} id is {self.id} and Gpa is {self.gpa}')

student1 = student('Antu',12,3.23)
student2 = student('opu',24,4.23)

student1.show_infp()
student2.show_infp()
class book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def is_long(pages):
        if pages > 200:
            return True
        else:
            return False
    def show_info(self):
        print(f'The Book Name Is {self.title}. The Author Name is {self.author}. And The Number Of Page is {self.pages}')
book1 = book('The Art Of Hard Work','Nepolion Hill',100)

book1.show_info()

class BankAcoount:
    def __init__(self,Holder_Name,balance):
        self.Holder_Name = Holder_Name
        self.balance = balance
    def choise(self):
        choise_c = input('Can You Want to Deposit Continue(y/n): ')
        if choise_c == 'y':
                amount = int(input('Enter Amount: '))
                self.balance = self.balance + amount
        else:
            print(f'Deposit Cancelled')

    def choise_w(self):
        choice_w = input('Do You Want to Withdraw(y/n): ')
        if choice_w == 'y':
                amount_w = int(input('Enter Amount: '))
                if amount_w <= self.balance:
                    self.balance = self.balance - amount_w
                    print(f'Withdraw Succesful Amount: {amount_w}')
                else:
                     print('Insufficiant Balance')
                     
        else:
            print('Withdrraw Canclled')
            print(f'Your Balance Is {self.balance}')
    def show_balance(self):
        print(f'Your Balance IS {self.balance}')
    
holder_1 = BankAcoount('Antu',0)
holder_1.choise()
holder_1.choise_w()
holder_1.show_balance()

class reactange:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        self.result =  self.length * self.width
        self.premite = 2*(self.length + self.width)
    def show_result(self)  :
        print(f'Your area is {self.result}')
        print(f'Your prmite is {self.premite}')
data = reactange(23,34)
data.area()
data.show_result()
class Memory:
    def __init__(self,name,age,status):
        self.name = name
        self.age = age
        self.status = status
    def __str__(self):
        return f"The Name Is {self.name} and the age is {self.age} and the status is {self.status}"
    def __len__(self):
        return len(self.name)
    def __getitem__(self, index):
        print(f'oh you want {index} number')
        return self.name[index]
    def show_data(self):
       print(f'{self.name} {self.age} {self.status}')

data1 = Memory('Antu',45,'student')
data2 = Memory('opu',45,'student')
data3 = Memory('coyon',45,'student')
data4 = Memory('ayon',45,'student')
data5 = Memory('chondon',45,'student')
data6 = Memory('Dipto',45,'student')
data7 = Memory('Abdullah',45,'student')
data8 = Memory('Biplob',45,'student')
data9 = Memory(['Mango','Orange','Apple'],34,'Employee')
data1.show_data()
data2.show_data()
data3.show_data()
data4.show_data()
data5.show_data()
data6.show_data()
data7.show_data()
data8.show_data()
print(data9[0])
    
import requests
import json 
url = 'https://www.google.com/'
new_post = {
    "Header" : "Search Topic",
    "POST" : input('Enter Search: ')
}
response = requests.post(url, json=new_post)
print(f'Status Code {response.status_code}')
print('Result: ')


print("Hello World!")
x = 10
print(type(x))
x = 10.5
print(type(x))
x = 'antu'
print(type(x))
x = True
print(type(x))
name = input('Enter Name: ')
print(f'Hello {name}')

num = int(input('Enter Number: '))
if num % 2 == 0:
    print(f'The Number {num} is Even')
else:
    print(f'The Number {num} is Odd')
for i in range(1,11):
    print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1

num_of_list = [1,2,3]
# num_of_list.append(4)

# print(num_of_list.pop())
num_of_list[1] = 5
print(num_of_list)


dict_of_num = {
    "name" : "Antu"
}
dict_of_num["Age"] = 23
dict_of_num["Status"] = "Fokirs"
# print(dict_of_num)
# key = dict_of_num.keys()
print(dict_of_num.values())

def add(a,b):
    return a + b

result = add(3,2)
print(result)

def multiply(a = 2, b = 3, c = 5):
    return a*b*c

result = multiply(5)
print(result)

def jog(*args):
    total = 0
    for num in args:
        total += num
    return total
result = jog(3,5,7,3,2,8,6,4,3,8,5,4,3,6,8,4,2,2,8)
print(result)

def employe(**kwargs):
    name = kwargs.get('Name','Opu')
    age = kwargs.get('Age',24)
    print(f'The Name is {name} And The Age Is {age}')
employe(Name = 'Antu')

def plus(**kwargs):
    return sum(kwargs.values())

result = plus(a = 3,b = 4)
print(result)
