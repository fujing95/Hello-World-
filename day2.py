#DAY 2 Understanding Data Types and How to Manipulate Strings
#data type
"hello"#string
"123"#string
123#integer
3.14159#float
True/False#boolean
123_456#integer("_"means","so it is 123,456)

#exercise 1 change data type
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

3+5 #output 8
7-2 #output 5
5*2 #output 10
6/3 #output 2.0(float)
2**3 #output 8
#PEMDAS calculation start from (),**,*,/,+,-

#exercise 2 BMI calculater
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
w = float(weight)
h = float(height)
print(int(w /(h * h)))

print(round(2.6666,2))#output: 2.67
print(int(2.6666))#output: 2
print(8//3)#type is integer,output: 2
print(8/3)#type is float,output: 2.677777...

#-=,+=,/=,*=
score += 1
score = score + 1
#line34,35 are the same meaning

#f-string method:simply change all data types into string,love it
score = 100
height = 1.8
iswinning = True
print(f'your score is {score},your height is {height},and your winning is {iswinning}')

#exercise 3 how many weeks you left
age = input("What is your current age?")
x = 90-int(age)
print(f'your left week number is {x*12}')

#Day 2 project: bill calculator
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
print('welcome to the tip calculator!')
total = float(input('what was the total bill?\n'))
per = int(input("what percentage tip you'd like to give? 10,12 or 15?\n"))
people = int(input('how many people to split the bill?\n'))
bill = (total/people*(1+per/100))
print(f'everyone should pay:{round(bill,2)}')
#output:everyone should pay:33.6
#2022.10.22FJ
