list = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]
avg = sum(list) / len(list)
var = sum((x-avg)**2 for x in list) / len(list)
print(var)