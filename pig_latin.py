text = input()
list = text.split(" ")
for i in list:
    print(i[1:]+i[0]+'ay', end=' ')   