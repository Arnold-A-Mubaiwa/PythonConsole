#simple operators
print(1+1+1)
print(12/8)
print(2*(3+4))

#datatypes
#float has a decimal number
print(9/2)
print(4*1.65)
print(1+2+3+4.0+5)

#Exponentiation is multiplying a number by itself
print(2**5)
print(9**(1/2))
print(8**(1/3))

#Quotient & Remainder
#Quotent return the larest possible number into a number
print(20//6)
#remainder
print(20%6)
print(7%(5//2))

#Modude Quiez
print(1+4*3)
print((3**2)//2)

#flight time
"""
    flying from LA - Sydney
    distance  = 7425 miles
    speed = 550 mile per hour
"""
print(7425/550)

#=============#
#   STRINGS   #
#=============#

#Backslash - to use qoutes in text
print("It\'s difficult until you start")

#Newline - to break a sentence
print("Let ta a break \nand continue")
print("""this
is a new line
and another one
let\'s say yah""")

#Concatenation
print(int("25")+int("76"))
print("spam"+" eggs")
print(6 *"hi")

#LEADERBOARD
i=1
while i<10:
    print(str(i)+".")
    i+=1

#=============#
#  Variables  #
#=============#

user= "Arnold"
print("User is : "+ user)
age = 22
print(age+ 4)
text= "This is text"
print(text+"!")

#input
x= input("Enter Input")
print(x)

num1 = int(input("Enter First NUmber"))
num2 = int(input("Enter Second Number"))

print(num1+num2)
num1*=num2
print(num1)

#TIP CALCULATOR
"""
    20% tip of the bill always

"""
bill = int(input("Enter Your bill"))
tip = bill*(20/100)
print(tip)

#Boolean True|False
my_boolean = True
print(my_boolean)


#Comparison Operators
x= 7
print(x!=8)
print(x>5)
print(x<2)
print(x>=7)
print(x<=7)

#if statement
num = 2
if(num>5):
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")
elif(num<5):
    print("Smaller than 5")
else:
    print("No")

#while loops
i  = 1
while i<5:
    print(i)
    if i>=2:
        break
    i+=1

i=3
while i>=0:
    print(i)
    i-=1

x=1
while x<100:
    if x%2==0:
        print(str(x)+ " is even") #explist convesion
    else:
        print(str(x)+ " is odd")
    x+=1

i = 5

while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

#BMI CALCULATOR
#BMI= W/H**2
weight = int(input("Enter your weight : "))
height = int(input("Enter your height : "))

BMI = weight/(height**2)
if BMI <=18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25 :
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obesity")

#=============#
#    Lists    #
#=============#

words = ["Hello","World","!"]
print(words[1])
nested = [
    [4,3,5],
    [6,8,7]
]
print(nested[0][2])

string index
stri= "Hello World"
print(stri[6])

nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)
print(1 in nums)

nums=[10,9,8,7,6,5]
nums[0]=nums[1]-5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

print(not 3 in nums)

#=============#
#  For loops  #
#=============#

for i in nums:
    print(str(i)+ "!")

str = "testing for loops"
count = 0

for x in str:
    if(x=="t"):
        count+=1

print(count)

#range
numbers = list(range(10))
print(numbers)

#range start and last
numbers= list(range(2,9,2))
print(numbers)

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6]) #2-6
print(squares[:7]) #0-7
print(squares[::2])
print(squares[::-1])
print(squares[1:-1])
print(squares[squares[2]])

Sum of Consecutive Numbers
N= int(input())
i=1
sum = 0;
while i<=N:
    sum +=i
    i+=1
print(sum)

sum=0
for i in range(N+1):
    sum+=int(i)
print(sum)

List Functions
num = [1,3,5,2,4]
print(len(num))

#useful functions
num.append(4)
print(num)

num.insert(3,10)
print(num)
print(max(num))
print(min(num))
num.append(1)
print(num.count(1))
num.remove(1)
print(num)

#String Formatting
print("max : {0} | min : {1}".format(max(num),min(num)))

#string functions
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

def my_func():
    print("spam")
    print("egg")
    print("spam")

my_func()

def print_with_exclamation(word):
    print(word+"!")
print_with_exclamation("Arnold")

#Search Engine

text = "My name is "
word = "name"

def search(x,y):
    a = 0
    list = x.split(" ")
    # for i in list:
    #     if(i == word):
    #         a += 1
    if word in list:
        return "found"
    else:
        return "Not found"
    # if(a==0):
    #     return "Word not found"
    # else:
    #     return "Word found"
        
print(search(text, word))