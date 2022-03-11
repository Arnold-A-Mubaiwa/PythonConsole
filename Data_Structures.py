#---------------------------#
#         String            #
#---------------------------#
print("hello there")
print("\tnew line")
x = "Arnold Mubaiwa"
print(x[3])
print(x[-2])
for i in x:
    print(i)

if "Arnold" in x:
    print("Arnold Available")

print("spam"+ "egg")
print(x*3)

#manipulating Strings

print(x.count('a'))
print(x.upper())
print(x.lower())
print(x.replace("Arnold","Anotida"))
print(x)
print(len(x))

text = "Good morning everyone"
letter = "o"
cont =0

for i in text:
    if (letter.upper() == i.upper()):
        cont+=1
print(cont)

#----------------------------------#
#              List  []            #
#----------------------------------#

names = ['James','Tom','Amy']
print(names[0])

m=[
    [2,3,4],
    [6,5,1],
    [8,9,7]
]
print(m[2][1])
print(5 in m[1])
print(len(m))

for n in names:
    print(n)

names.append(8)
names.remove("Tom")
print(names)
x = [8, 5, 42, 11, 20, 4]

x.sort()
print(x)
print(max(x)-min(x)+x[2])

cubes  = [i**3 for i in range(5)]
print(cubes)

text = "sololearn in awesome"
length=len(text)
list= text.split(" ")
l_len= len(list)
for i in text:
    if i==" ":
        length-=1
print(float(length/l_len))

# Dictionaries {key:value}
ages = {
    "Dave":10,
    "John":20,
    "Maty":35
}
print(ages['Dave'])
print(ages["Maty"])
print(ages.get('Dave'))
print(len(ages))

fib= {1:1,2:1,3:2,4:3}
print(a:=fib.get(4,0))
print(b:=fib.get(7,5))
print(a+b)

# Tuples - cannot be changed ()

words =  ("spam", "eggs","milk")
print(words[1])
# words[1]="cheese" (can't assign new value to tuples)
#tuples can be used as keys for dictinary unlike lists

dict={
    ("David",42):"red",
    ("Bob",24):"green"
}
print(dict[("David",42)])
a,b,c = words
print(a)
print(c+b)
c,b=b,c
print(c+b)
x, y = [1, 2]
x, y = y, x
print(x)

# Sets are unique {}

nums={1,2,3,4,5,6}
print(nums)
nums.add(-7)
nums.remove(4)
print(nums)

sec = {9,8,7,6}
print(nums | sec)
print(nums & sec)
print(nums- sec)
print(nums^sec)

# User-Defined DataStructures

# Stacks
# uses LIFO last in first out

class Stack:
    def __init__(self):
        self.items  = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0,item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)

s = Stack()
s.push(7)
s.push('b')
s.push('7')
s.push(True)
s.print_stack()
s.pop()
s.print_stack()

# Queue uses FIFO first in first out
# The process of adding new elements is called enqueue 
#the process of deleting elementv is called dequeue

class Queue:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items ==[]
     
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()

# Linked Lists

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data,None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)
    
    def get_last_node(self):
        n = self.head
        while (n.next != None):
            n = next
        return n.data

    def is_empty(self):
        return self.head == NotImplemented

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end='=>')
            n = n.next
        print()

s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(10)

s.print_list()

class Graph(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 1 
            self.adj[dest-1][orig-1] = 1 
        
    def remove_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 0 
            self.adj[dest-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(4) 
G.add_edge(1, 3) 
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()


# Ticket Office
data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input())
#your code goes here

def get_sum(x):
    sum = 0
    for a in data.values():
    # print(a)
        if a <x:
            sum+=5
        elif a>= x:
            sum+=20
    return sum

def calculate():
    actual = get_sum(18)
    adjusted = get_sum(age)
    total = int(((adjusted-actual)/actual)*100)
    return total

print(calculate())

# Balanced Parethesis

def balanced(expression):
    list =[]
    #your code goes here
    for char in expression:
        if char == "(":
            list.insert(0,char)
        elif char == ")":
            if list != []:
                list.pop(0)
            else:
                return False
    if list != []:
        return False
    else:
        return True

print(balanced(input()))