info = {
    'name':input('Enter Name: '),
    'age': int(input('Enter Age: '))
}

info['name'] = 'Chondon'
info['name'] = 'Dipto'
print(info['name'])
student = {
    'name': 'Antu',
    'age' : 24,
    'Subject': {
        'phy': int(input('Enter marks: ')),
        'chem' : int(input('Enter Marks: ')),
        'bio': int(input('Enter Marks: '))
    }
}
student['Subject']['phy'] = 90
print(student)
print(student['Subject']['phy'])
print(student.keys())
print(list(student.values()))
def function(a,b):
    return a+b,a-b,a*b
x,y,z = function(10,8)
print(x)
print(y)

money = 100
def change_money():
    global money
    money = 500
change_money()
print(money)
def local_var():
    local = 'I am Antu'
    print(local)
local_var()
local_var()
local_var()
local_var()
local_var()

my_list = []
def change():
    my_list.append('*')
    print(my_list)
change()
change()
change()
change()
money = 100
def change_moneyh():
    money = 500
def change_nmoney():
    global money
    money = 500
change_nmoney()
print(money)
i = 1
def outer():
    count = 0
    global i
    def inner():
        nonlocal count
        count += 1
        print(count)
    while i < 100:
        inner()
        i += 1
outer()
add = lambda a,b: a + b
print(add(6,5))
try:
    def add(a,b):
        return a + b
    
    result = add(5,2)
    print(result)
    mongo = add(9,89)
    print(mongo)
except:
    print('Sorry it not possible')
list_numbers = [1,2,3,4,5,6,7,8,9,10]
rio = list(map(lambda x: x**2,list_numbers))
print(rio)
num = map(lambda x: x**2,range(1,11))
print(list(num))
list_of_num = list(filter(lambda x:x % 2 ==0,range(1,100)))
print(list_of_num)
numbers = []
for i in range(1,1000):
    numbers.append(i)
print(list(filter(lambda x: x % 5 == 0,numbers)))
print(list(filter(lambda x: x%5==0,range(1,1000))))
Law Of Comprehension
1.[ expression  for item in iterable  if condition ]



#Project 1
marks = []
for i in range(3):
    sub = int(input('Enter Marks: '))
    marks.append(sub)
# Part 1 
total = 0
def total_n():
    global total
    for mark in marks:
        total = total + mark
#Part 2
    averege = total/len(marks)
    if averege >= 80:
        print('A+')
    elif averege >= 60:
        print('A')
    elif averege >= 40:
        print('B')
    else:
        print('C')
total_n()



#Project 2
list_of_num = []
for i in range(1,11):
    list_of_num.append(i)
#Part 1
even = list(filter(lambda x: x % 2 == 0,list_of_num))
sqr = list(map(lambda y: y**2,even))
print(sqr)


List Comprehension
mat = [x for x in range(1,11) if x % 2==0]
sqrn = list(map(lambda x: x**2,mat))
print(sqrn)

List Comprehension 
nrt = [x**2 for x in list_of_num if x % 2 == 0]
print(nrt)
