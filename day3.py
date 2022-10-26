#exercise 1 odd or even check
number = int(input("Which number do you want to check? "))
if number % 2 > 0:# % sign means divided and find the modulo
  print('This number is odd')
else:
  print('This number is even')

# = is different from ==
height = 120# put 120 inside height variable
height == 120# check if height equals to 120
height != 120# !=means not equal to

#if,elif,else
if condition A:
    do A
elif condition B:
    do B
else:
    do C

#BMI calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
w = float(weight)
h = float(height)
BMI = float(w /(h * h))
if BMI < 18.5:
  print('you are underweight')
elif BMI < 25:
  print('you have a normal weight')
elif BMI < 30:
  print('you are slightly overweight')
elif BMI < 35:
  print('you are obese')
else:
  print('you are clinically obese')

#Exercise 2 leap year indicator
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print('leap year')
    else:
      print('not a leap year')
  else:
    print('leap year')
else:
  print('not a leap year')

#Exercise 3 pizza bill calculator
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
elif size == 'L':
  bill += 25
if add_pepperoni == 'Y':
  if size == 'S':
    bill += 2
  else:
    bill += 3
if extra_cheese == 'Y':
  bill += 1
print(f'your final bill is ${bill}')

#Exercise 4 Truelove calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
lname = name.lower()
t = lname.count('t')
r = lname.count('r')
u = lname.count('u')
e = lname.count('e')
l = lname.count('l')
o = lname.count('o')
v = lname.count('v')
e = lname.count('e')
true = t + r + u + e
love = l + o + v + e
score = int(str(true) + str(love))
if score < 10 or score > 90:
  print(f'score is {score}, your two are like coke and mentos')
elif 40 < score < 50:
  print(f'your score is {score}, you are alright together')
else:
  print(f'your score is {score}')

#Day3 project:treasure island game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('you\'re at a cross road，where do you want to go，type "left" or "right".\n').lower()
if choice1 == 'left':
  choice2 = input('you\'ve come to a lake, there is an island in the middle of the lake. Type wait to "wait" for a boat, type "swim" to swim across.\n')
  if choice2 == 'wait':
    choice3 = input('you arrive at the island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which color do you choose?\n')
    if choice3 == 'yellow':
      print('you found the treasure,you win!')
    elif choice3 == 'red':
      print('you burned by fire,game over')
    elif choice3 == 'blue':
      print('you enter a room full of beasts,game over')
    else:
     print('you choose a door that doesn\'t exsit,game over')
  else:
    print('you got attacked by an angry trout, game over')
else:
 print('you fell into a hole，game over.')


print('''

                               ,----.
                              ( WOW! )                         .-.
                               `----' _                         \ \
                                     (_)                         \ \
                                         O                       | |
                    |\ /\                  o                     | |
    __              |,\(_\_                  . /\---/\   _,---._ | |
   ( (              |\,`   `-^.               /^   ^  \,'       `. ;
    \ \             :    `-'   )             ( O   O   )           ;
     \ \             \        ;               `.=o=__,'            \
      \ \             `-.   ,'                  /         _,--.__   \
       \ \ ____________,'  (                   /  _ )   ,'   `-. `-. \
        ; '                ;                  / ,' /  ,'        \ \ \ \
        \                 /___,-.            / /  / ,'          (,_)(,_)
         `,    ,_____|  ;'_____,'           (,;  (,,)      jrei
       ,-" \  :      | :
      ( .-" \ `.__   | |
       \__)  `.__,'  |__)  SSt

''')
