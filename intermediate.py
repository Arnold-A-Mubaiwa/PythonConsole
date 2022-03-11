n= [2,4,6,8]
res = 1

for x in n[1:3]:
    res*=x

print(res)

#Dictionaries
#=============

#list - has an index that starts from 0 []
x =["hi","there", "arnold"]
print(x[2])

#dictionary - key to value pairs {}
ages={
    "Dave":24,
    "Mary":42,
    "John":58
}
print(ages["Dave"])

cars={
    "BMW": "BLUE",
    "VOLVO": "RED"
}

if ("BMW" in cars):
    print("BMW car color is {0} ".format(cars["BMW"]))

#using get
data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

country = "Ireland"

if country in data:
    print(data.get(country))
else:
    print("Not found")

fib = {1:1,2:1,3:2,4:3}
print(fib.get(4,0)+ fib.get(7,5))

#Tuples are like list but cannot be changed and
#they use parenthesis()
#they can be used without parenthesis
words = ("spam", "eggs", "sausages",("hi","there","arnold"))
print(words[1])
print(words[3][2])

newTuple = "one","two","arno",1,2,3,5,9
print(newTuple[1])

#Tuple Unpacking
a,b,c,*num = newTuple
print("a : {0}, b : {1}, c : {2}".format(a,b,c))
a,c = c,a
print(c)
print(num)
print(len(num))

#set - are like lists and dictionary - {1,2,3}|  no duplicates
num_sec= {1,2,3,4,5}
num_fir = {4,5,6,7,8,9}
print(3 in num_sec)
num_sec.add(10)
num_sec.remove(1)
print(num_sec)
print(num_fir | num_sec)
print(num_fir & num_sec)
print(num_fir - num_sec)
print(num_fir^num_sec)

cubes= [i**2 for i in range(10) if i**2 % 2 == 0]
print(cubes)

#Letter Counter
text = input()
dict = {}

for letter in text:
   if letter != " ":
    if(letter not in dict):
        dict[letter]=1
    else:
        dict[letter]=dict.get(letter)+1


print(dict)
    
#=============================#
#  Functional Programming    #
#=============================#

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five, 10))


#Pure function
def func(x):
    y=x**2
    z=x+y
    return z

print(func(5))

#Lambdas
print((lambda x: 2*x*x)(4))

#map creates a new function from an iterable
#following instructions appllyed to it
nums = [11,22,33,44,55]
result = list(map(add_five,nums))
print(result)

#map on lambdas
result= list(map(lambda x: x+5,nums))
print(result)

#filter on lambdas
result = list(filter(lambda x: x==22, nums))
print(result)

#Generators
#uses yield

def decor(func):
    def wrap():
        print("---------------------------")
        func()
        print("---------------------------")
    return wrap

def print_text():
    print("Hello Word")

decorator = decor(print_text)
decorator()

@decor
def decor_line():
    print("Using the @decor line")

decor_line()

def fib(x):
    
  if x == 0 or x == 1:

    return 1

  else: 

    return fib(x-1) + fib(x-2)

print(fib(4))

def power(x, y):
    
  if y == 0:

    return 1

  else:

    return x * power(x, y-1)

print(power(2, 3))

#Spelling Backwards

def spell(txt):
    length = len(txt)-1
    while length>=0:
        print(txt[length])
        length-=1
txt = "hello"
spell(txt)                                    


#---------------------#
#      CLASSES       #
#---------------------#

class Dog:
    def __init__(self,color,legs):
        self.color = color;
        self.legs = legs

    def bark(self):
        print("woof!  woof!")

felix = Dog("Ginger", 4)
rover = Dog("Dog-Colored", 4)
stumpy = Dog("Brown",4)
print(felix.color)
felix.bark()

class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Puur");

kiti = Cat("Kiti", "Blue")
print(kiti.color)
kiti.purr()

#Magic Methods should revisit
class Vector2D:
    def __init__(self,x,y):
        self.x  = x
        self.y= y
    def __add__(self,other):
        return Vector2D(self.x + other.x , self.y + other.y)

first = Vector2D(5,7)
print(first)
second  = Vector2D(3,9)
result = first+ second
print(result.x)
print(result.y)

class specialstring:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "="*len(other.cont)
        return "\n".join([self.cont,line, other.cont])

spam =specialstring("spam")
hello = specialstring("Hello World")
print(spam/ hello)

#Data Hinding- Encapsulation
#Weak _|
class Queue:
    def __init__(self, contents):
        self._hiddenlist  = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue  = Queue([1,2,3,4,5])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue._hiddenlist)

#Strongly __|
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
# print(s.__egg)


FILES
file= open("newfile.txt")
open("newfile.txt" ,"r") read
open("newfile.txt" ,"w") write
open("newfile.txt" ,"wb") writebinary
cont = file.read()
print(file.read(5))
print(file.read(7))
print(cont)

for line in file.readlines():
    print(line)
file.close()

file= open("newfile.txt", "a"):

file.write("making changes")
file.close()

file = open("file.txt")

for li in file:
    st = list(li.split(" "))
    string=''
    for i in st:
        string += i[0]
    print(string)
    
file.close()