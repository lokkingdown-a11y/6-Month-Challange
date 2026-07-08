name = input('Enter Your Name: ')
age = int(input('Enter Age: '))
print(f'Welcome {name}')
print(f'After 20 Years Your Age is {age+20}')
list_n = [5,7,8,9,5,10,20,2,30]
min = list_n[0]
max = list_n[4]

if min > list_n[1]:
    min = list_n[1]
if min > list_n[2]:
    min = list_n[2]
if min > list_n[3]:
    min = list_n[3]
if min > list_n[4]:
    min = list_n[4]
if min > list_n[5]:
    min = list_n[5]
if min > list_n[6]:
    min = list_n[6]
if min > list_n[7]:
    min = list_n[7]
if min > list_n[8]:
    min = list_n[8]


if max < list_n[1]:
    max = list_n[1]
if max < list_n[2]:
    max = list_n[2]
if max < list_n[3]:
    max = list_n[3]
if max < list_n[4]:
    max = list_n[4]
if max < list_n[5]:
    max = list_n[5]
if max < list_n[6]:
    max = list_n[6]
if max < list_n[7]:
    max = list_n[7]
if max < list_n[8]:
    max = list_n[8]

print(f'Your Small Num Is {min}')
print(f'Your Max Num is {max}')
list_n = [5,7,8,9,5,10,20,20,30,70,80]
min = list_n[0]
max = list_n[0]
for i in list_n:
    i = 0
    while i < len(list_n):
        if min > list_n[i]:
            min = list_n[i]

        i = i + 1

for i in list_n:
    i = 0
    while i < len(list_n):
        if max < list_n[i]:
            max = list_n[i]
        i += 1


print(f'Your Min Value Is {min} ')
print(f'Your Max Value Is {max} ')
list_n = [5,7,8,9,5,10,20,20,30,70,80]
min = list_n[0]
max = list_n[0]
for x in range(len(list_n)):
    if x < len(list_n):
        if min > list_n[x]:
            min = list_n[x]

for x in range(len(list_n)):
    if x < len(list_n):
        if max < list_n[x]:
            max = list_n[x]

print(f'Your Min Value is This {min} ')
print(f'Your Max Value Is This {max} ')


total = 0 
for i in range(2,102,2):
    total += i

print(f'Your Adittion Is This {total}')

name = input('Enter Name: ')
print(f'Hello {name}')

def con():
    while True:
        name = input('Enter Name: ')
        print(f'Hello {name}')
        while True:
            con = input('Can You Continue Y/N: ')
            if con.lower() == 'y':
                print(f'Hello {name}')
                break
            else:
                print(f'Bye Bye {name}')
                return
con()
while con != 'n':
    con()
    if con == 'n':
        break
