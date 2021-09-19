vaccinated = {
    'never':5,
    'once':8,
    'twice':4,
    '3 times':3
}
totalv =0
for v in vaccinated.keys():
    if v == 'never':
        totalv += 0
    elif v == 'once':
        totalv += (vaccinated[v])
    elif v == 'twice':
        totalv += (vaccinated[v]*2)
    elif v == '3 times':
        totalv+= (vaccinated[v]*3)
    else:
        continue
print(int(totalv/20) )  