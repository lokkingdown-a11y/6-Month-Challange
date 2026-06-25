try:
    number = int(input('Enter Number: '))
    print(1/number)
except ZeroDivisionError:
    print('1 Can not devided by 0 idiot')
except ValueError:
    print('Please Enter Intiger Number Only')
finally:
    print('Do You Some Clean Up')
continue_program = input('y/n: ')
while continue_program != 'n':
Project 4
num = int(input('Enter Number: '))
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')
def function():
    continue_program = input('continue: y/n: ')
    while continue_program != 'n':
        if continue_program == 'y':
            num = int(input('Enter Number Again: '))
            for i in range(1,11):
                print(f'{num}x{i} = {num*i}')
            continue_program = input('continue: y/n: ')
        if continue_program == 'n':
            print('Program Stoped')
            break
function()

def function():
    phonebook = []
    name = input('Name: ')
    phone_number = input('Enter Phone Number: ')
    phonebook.append(name)
    phonebook.append(phone_number)
    print(phonebook)
    while True:
        c_b = input('Are You Continue: (y/n): ')
        if c_b == 'y':
                name = input('Name: ')
                phone_number = input('Enter Phone Number: ')
                phonebook.append(name)
                phonebook.append(phone_number)
                print(phonebook)
        else:
             print('Program Stoped')
             break
        
    find = input('Enter Name: ')
    for find in phonebook:
        if find in phonebook:
             print(f'The {find} is Available')
        else:
             print(f'The {find} is not Avilable')
function()
Task 1
def pass_generator():
    while True:
        password = input('Enter Pass: ')
        if len(password) < 8:
            print('Password Is weak')
        else:
            print(f'The {password} is strong')
            break
pass_generator()

Task 2
number = int(input('Enter Number: ' ))
list_n = []
for i in range(1,number+1):
    list_n.append(i*i)

print(list_n)

Task 3
list_of_num = [-5, 3, -1, 8, 0, -2, 7]
pos = list(filter(lambda x: x > 0,list_of_num))
print(pos)


Task 4
cophen = [x*2 for x in range(1,21)  if x % 2 == 0]
print(cophen)

Task 5
u_i = int(input('Enter Num: '))
i = 1
while i <= u_i:
    print(i)
    i += 1

Task 6

f_dic = {
    'Name': [input('Enter Name: ')],
    'Age' : [int(input('Enter Age: '))]
}
for i in range(1,4):
    f_dic['Name'].append(input('Enter Name: '))
    f_dic['Age'].append(int(input('Enter Age: ')))
print(f_dic)

Task 7 
numbers = [12, 7, 9, 24, 5, 18, 3, 20]
even = list(filter(lambda x: x % 2 == 0,numbers))
odd = list(filter(lambda y: y % 2 != 0, numbers))
print(f'Even Numbers: {even}')
print(f'Odd Numbers: {odd}')
