x = [1,2,3,4,5,6]
print(x[0])
multi_x=[
    x,
    ['a','b','c','d']
]
print(multi_x[0][2])

print(1 in x)
print(10 in x)

# task
data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = 'blue'
#your code goes here
colors = ['brown','blue','green','black']
if color.lower() in colors:
    i = colors.index(color)
    c_value =0 
    total=0
    for num in data:
        for n in num:
            total+=n
        c_value+= num[i]
    print(int((c_value/total)* 100))

x.reverse()
print(x)
x.sort()
print(x)

# task
prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
#your code goes here
total=0
aver=int(sum(prices)/len(prices))
for n in prices:
    if n>aver:
        total+=1

print (total)

cubes = [i**3 for i in range(5)]
print(cubes)
nums = [i*2 for i in range(10)]
print(nums)
print([i*2 for i in range(10) if i**2 % 2 ==0])