'''
dumb_word = ""
for letter in "supercallafragalisticexpialadocious":
  if letter > "m":
    dumb_word += letter
print(dumb_word)

name = input("What is your name? ")
print(name)
print(type(name))

age = int(input("What is your age? "))
print(age)
print(type(age))

print("I am " + str(age) + " years old.")

print(name * age )
print(2 ** 3)
print(type(4/2))

x = "Lev"
y = 17
print("My name is " + x + " and I am " + str(y) + " years old. ")
print(f"My name is {x} and I am {y} years old.")

#Evaluating expressions
x = 5 
y = 3
print(f"The sum of x and y is {x + y}")

#Rounding floats in f-strings
import math
math.pi
print(f"Pi to two decimal places is {math.pi:.2f}")

#Expressing a float as a percentage
x = 0.389657
print(f"{x:%}")
print(f"{x:.0%}")
print(f"{x:.3%}")

#Booleans and stuff
x = True
print(type(x))

print("Is x true or false? " + str(x))

x = True
y = False
print(x and y)
print(x or y)
print(not x or y)
print(x and not y)
print(not(x and y))
print(not x or not y)

x = True
y = False
z = False

print(x or y)
print(y and z)
print(x or(y and z))
print((x or y) and z)
print(x or y or z)

# If statements 
x = 5
y = 12
if x > 12:
  print("monty")
elif y <= 8:
  print("python")
else:
  print("flying circus")

#yay finally smth to code
age = input("What is your age? ")
day = input("What day of the week is it? ")

if day == "Saturday" or day == "Sunday":
  print("Stay at home")
elif int(age) > 18:
  print("Go to work")
elif int(age) > 4:
  print("Go to school")
else:
  print("Stay at home")

print(0.1 + 0.2)
from decimal import *
print(0.1 + 0.2)
print(Decimal(.3))

for i in range(1, 6, 2):
  if i**2 == 9:
    continue
  print (i**2)
for i in "Hello World":
  print (i)
x = [3, 6, 9]
for i in x:
  print(i)
i = 1
while i < 20:
  print(i*2)
  i = i+2

#challenge problems or smth
x = 1
for i in range(1, 6):
  x *= i 
print(x)

for i in range(100):
  if i % 7 == 0:
    print(i)

x = 0
while x < 2:
  first = input("What planet do we live on? ")
  second = input("What state do we live in? ")
  if first == "earth" and second == "indiana":
    x = 2

from random import *
while True:
  dice1 = randint(1,6)
  dice2 = randint(1,6)
  print(str(dice1))
  print(str(dice2))
  if dice1 == 6 and dice2 == 6:
    break

string = "Hello World"
x = 0
letter = False
for i in string:
  if letter == True and i == "l":
    x += 10
  elif letter == False and i == "l":
    x += 1
    letter = True
  else:
    letter = False
print(x)
for i in range(1,7):
  for j in range(1,7):
    print(f"{i}, {j}")
for i in range(11):
  for j in range(11):
    if i == 2 and j == 2:
      print(" |X", end="")
    else:
      print(" | ", end="")
  print("")
x = "Global variable or smth"
def function():
  x = "woah local variable!"
  print(x)
function()
print(x)
def func_a():
  return func_b()*3
def func_b():
  return func_c() * 2
def func_c():
  return 1
x = func_a()
print(x)
def func_r(x):
  if x<5:
    print(f"Going up: {x}")
    func_r(x+1)
    print(f"Coming down: {x}")

func_r(1)
def factorial(n):
  if n == 1:
    return n
  else:
    return n * factorial(n-1)

print(factorial(5))
def add_two(x):
    return x + 2
def times_three(x):
  return x * 3
def function(x):
  return add_two(times_three(x))
print(function(5))
def add(x,y=5):
  print(x+y)
add(10)
def ask():
  try:
    age = int(input("What is your age?: "))
    print(f"Your age is {age}")
  except ValueError:
    print("That is not an integer.")
ask()

def div0(x,y):
  try:
    print(x/y)
  except ZeroDivisionError:
    print("Can't divide by zero")
div0(0, 0)
s = "one ring to rule them all"
print(s)
print(s[0])
print(s[10])
print(len(s))
#print(s[50]) doesn't work, out of index length
print(s[-1])

print(s[5:10])
print(s[0:6])
print(s[-23:-19])
print(s[5:])
print(s[:5])
print(s[:20])
#cannot change strings
s = "hello" #s = "jello"
s[0] = "j"
print(s)
def Modify_String(word, letter):
  return letter + word[1:]
print(Modify_String("Bat","H"))
from string import ascii_lowercase as a_low 
text = "Bee Movie"
print(text.lower())
if "e" in a_low:
  print("e is in the alphabet")

#for i in a_low:
  #print(i)

def Counting(word):
  x = 0
  for i in word:
    if i in a_low:
      x += 1
  print(f"there are {x} letters in this string")    

def specCounting(x, y):
  z = 0
  for i in x:
    if i == y:
      z += 1
  print(f"There are {z} '{y}'s in this word")
specCounting("what the hell", "h")
from string import ascii_lowercase as a_low

file = open('plainTextGettysburgAddress.txt', 'r')

def LettersInAlphabet(x):
  n = 0
  for i in x.lower():
    if i in a_low:
      if i == "a":
        print("A = 1")
      n += 1
  return(n)
  
fox = "The quick brown fox jumps over the lazy dog"

print(LettersInAlphabet(fox))

def find(string, sub_string):
  count = 0
  i = 0
  for j in string:
    if string[i:i+len(sub_string)] == sub_string:
      count += 1
      print(f"There is a {sub_string} at {i}")
    i += 1
  print(f"There are {count} {sub_string}s")

find(file.read(), "and")

import math
import cmath

#math.ceil prints the nearest integer greater than or equal to x
print(math.ceil(0.5))

#math.floor prints the nearest integer lower than or equal to x
print(math.floor(0.5))

#math.comb returns the number of possible groups of y within a group of x
print(math.comb(5,3))
#here's a visual representation of what's being calculated:

AAABB
AABAB
AABBA
ABAAB
ABABA
ABBAA
BAAAB
BAABA
BABAA
BBAAA

#math.fabs just prints the absolute value of a number
print(math.fabs(-10))
#math.factorial prints the value of a number times every above 0 integer below the it 
print(math.factorial(5))

#isinf, isfinite, and isnan all return true or false values depending on x's value.
#isinf returns true if the value is infinite (includes -inf)
print(math.isinf(float('inf')))
#isfinite returns true if the value is finite
print(math.isfinite(10))
#isnan returns true if the value is not a number
print(math.isnan(float('nan')))

#math.pow lets you raise a value x to the power y
print(math.pow(2,2))
#math.sqrt lets you return the square root of a function
print(math.sqrt(4))

#essentially, logarihtmic functions return the exponent required
#for their base to turn into the argument
# logA (x) = b,    A ^ b = x
#math.log10 accepts one argument ("x" in the example above)
#math.log accepts 2 arguments, the first being x, and the second being the base (or A)
print(math.log10(100))
print(math.log(100,10))

from fractions import Fraction

print(Fraction(6,24))

print(Fraction(113,100) + Fraction(25,18))

print(Fraction(1.13))

import math
print(Fraction(math.pi))

print(Fraction('1.1'))
print(Fraction('1000.56'))

from decimal import *

decimal_number1 = Decimal('3.14')
decimal_number2 = Decimal('2.718')

print(decimal_number1 + decimal_number2)

print(round(5.123699, 4))

dec = Decimal("2.35").quantize(Decimal("1.0"))
print(dec)

import calendar
print(calendar.weekheader(3))
print("")
print(calendar.firstweekday())
print(calendar.month(2024,3))
print(calendar.monthcalendar(2024,3))
print(calendar.calendar(2024))
day_of_the_week = calendar.weekday(2024,2,26)
print(day_of_the_week)
print(calendar.leapdays(2000,2024))

import datetime
from datetime import timedelta
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(datetime.datetime(2024,2, 28))
today = datetime.now()
print("Today: ", str(today))
after2years = today + timedelta(days=730)
print("Date after 2 years: "+ str(after2years))
hi = datetime.time()
print(hi)
hello = datetime.time(12,30,45)
#aware dates include timezone data, naive dates return UTC
import pytz
#timezone shit.
current_date = datetime.datetime.now(pytz.timezone('US/Eastern'))
print(current_date)

import statistics as stats
test = [1,4,2,3]
print(stats.harmonic_mean(test))
print(stats.mean(test))
print(stats.median(test))
#highest number closest to the median
stats.median_high(test)
#lowest number losest to the median
stats.median_low(test)
stats.mode(test)
#population and sample standard deviations
#stats.pstdev(test)
stats.variance(test)
import random
print(random.randrange(1,10))
print(random.choice(['yes','no','maybe']))
order = 'a b c d'.split()
random.shuffle(order)
print(order)
print(random.uniform(1.0,2.0))
print(random.sample([2,4,7,12,100,89,23], k =2))
#k is how many numbers picked

x = input("enter a number 1-10 ")
y = random.randrange(1,10)
if x == y:
  print("You win!")
elif x != y:
  print("You didn't win!")
  print(y)
else:
  print("error")

#teams = ["Colts", "Patriots", "Bears"]
#teams.append("Steelers")
#teams.insert(1,"Steelers")
#del teams[-1]
#teams.remove("Patriots")
#teams.pop()
#first_team = teams.pop(0)
#print(teams)
#print(first_team)
##string_teams = "Ravens Cowboys Falcons"
##print(string_teams.split(" "))
##print(" ".join(teams))
##teams2 = string_teams.split(" ")
##teams.extend(teams2)
###teams.reverse()
###print(teams)
###teams.sort()
###print(teams)
###print(teams.count("Colts"))
teams = ["Colts", "Bears", "Chiefs", "Ravens", "Saints"]
#for i in teams:
 # if i == "Colts":
  #  print(f"My favourite team is {i}")
  #else:
   # print(f"{i} stink!")

#for index, value in enumerate(teams):
  #print(f"{value} is in the {index} index of my list")

num = [10, 15, 35, 20, 22]
new_list = []
for index, value in enumerate(num):
  if value % 2 == 0:
    new_list.append(index)
print(new_list)

from string import ascii_lowercase as a_low

new_alpha = ""
for i in a_low:
  new_alpha = new_alpha + i + " "
alpha_list = new_alpha.split(" ")
alpha_list.pop(-1)
print(alpha_list)

vowel_list = ["a","i","u","e","o"]
for index, value in enumerate(alpha_list):
  if value in vowel_list:
    print(f"{index} index, {value}")
    
zach = "Zach has hair and Zach has eyebrows"
for index, value in enumerate(zach.split(" ")):
  if value == "Zach":
    print(f"{index}, {value}")

grid = [
  [0]*3,
  [1]*3,
  [2]*3
]
for i in range(len(grid)):
  print(grid[i])

perfect_squares = []
for i in range(1,10,1):
  perfect_squares.append(i**2)
print(perfect_squares)

perfect_squares2 = [i**2 for i in range(1,10,1)]
print(perfect_squares2)

div_list = [i%2 == 0 or i%3 == 0 for i in range(0,11)]
print(div_list)

div_list2 = [i for i in range(0,11) if i%2==0 or i%3==0]
print(div_list2)

my_list = ["item0","item1","item2"]
x, y, z = my_list
print(x)
print(y)
print(z)

def math(x,y,z):
  print(x + y + z)
my_list = [1,2,3]
math(*my_list)

#creates 2 objects, same value. Same value, different identities
a = ["premiere", "deuxieme"]
b = ["premiere", "deuxieme"]
print(a == b)
#makes c refer to the same object as b. Same value, same identity
c = b
print(c == b)
print(a is b)
print(c is b)
print(id(a))
print(id(b))
print(id(c))

a = ('boom','bang')
b = ('boom','bang')
print(a is b)
a = 'boom'
b = 'boom'
print(a is b)
a = 500
b = 500
print(a is b)

def my_func(some_list):
  some_list.append("RAHH")

a = ["woah.", "wowww"]
my_func(a)
print(a)

class DryErase:
  def __init__(self,color,size,tip):
    self.color = color
    self.size = size
    self.tip = tip
  def draw(self):
    print("You drew a line on the board")

marker1 = DryErase("blue","medium","normal")
print(marker1.color)

marker1(draw)
'''
import requests
import json

response = requests.get("https://randomuser.me/api/")
print(type(response))
print(response)
print(response.text)
print(type(response.text))

response_json = json.loads(response.text)
print(type(response_json))

person = response_json['results'][0]

for key in person:
    print(f"{key}: {person[key]}")  