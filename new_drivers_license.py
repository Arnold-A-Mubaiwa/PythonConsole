name = input('Enter your name : ')
agents = int(input('Enter number of Agents : '))
list = input('Enter names separated with space : ').split(' ')
sum = 0
for i in list:
    if i < name:
        sum+=1
print(((sum//agents)+1)*20)