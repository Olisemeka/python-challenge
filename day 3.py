# print('Welcome')
# no = int(input('What number do you want to check? '))
# check = no % 2

# if check == 0:
#     print('This is a "EVEN" number.')
# else:
#     print('This is a "ODD" number.') 


# print('Welcome to the roller coaster system')
# height = int(input('Enter your height in cm '))
# if height >= 120:
#     print('HURRAY !!! Can ride')
#     age = int(input('How old are you? '))
#     if age <= 12:
#         print('You are to pay $5.00')
#     elif age < 18:
#         print('You are to pay $7.00')
#     elif age >= 45 and age <= 55:
#         print('You have earned a free ticket')
#     else:
#         print('You are to pay $12.00')
# else:
#     print('Oh no oo! You need to grow taller')



# year = int(input('Which year do you want to check \n'))
# if year % 4 == 0:
    
#     if year % 100 != 0:
#         if year % 400 == 0:
#             print('Leap Year')
#         else:
#             print('Not leap Year')
#     else:
#         print('Leap Year')
# else:
#     print('Not Leap Year')



# print('Welcome to Pizza Deliveries system')
# bill = int(0)
# size = input('Which kind of pizza do you want? S, M or L ')
# if size == "S":
#     bill += 15
#     add_pepperoni = input('Do you want to add pepperoni? Y or N ')
#     if add_pepperoni == "Y":
#         bill += 2
        
# elif size == "M":
#     bill += 20
#     add_pepperoni = input('Do you want to add pepperoni? Y or N ')
#     if add_pepperoni == "Y":
#         bill += 3
# elif size == "L":
#     bill += 25
#     add_pepperoni = input('Do you want to add pepperoni? Y or N ')
#     if add_pepperoni == "Y":
#         bill += 3
# extra_cheese = input('Do you want to and extra-cheese? Y or N ')
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}")



print('Welcome to love Caculator')
name1 = input('What is your name \n').lower()
name2 = input('What is their name \n').lower()
t1 = name1.count("t")
t2 = name1.count("r")
t3 = name1.count("u")
t4 = name1.count("e")
t_value = (t1 + t2 + t3 + t4)

r1 = name1.count("l")
r2 = name1.count("o")
r3 = name1.count("v")
r4 = name1.count("e")
r_value = (r1 + r2 + r3 + r4)

value2 =(t_value + r_value) 


q1 = name2.count("t")
q2 = name2.count("r")
q3 = name2.count("u")
q4 = name2.count("e")
q_value = (q1 + q2 + q3 + q4)
 
l1 = name2.count("l")
l2 = name2.count("o")
l3 = name2.count("v")
l4 = name2.count("e")
l_value = (l1 + l2 + l3 + l4)
value =(q_value + l_value)

if value2 <= 1 or value2 >=9:
    print(f"Your score is {value2}{value}%, You go together like coke and  mentos.")
elif value2 >= 4 and value2 <= 5:
    print(f"Your score is {value2}{value}%, you are alright together.")
else:
    print(f"Your score is {value2}{value}%.")