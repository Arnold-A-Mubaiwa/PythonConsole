x='Brian\'s mother: He'
print(x)
print(x[3])
print(x[-1])

for c in x:
    print(c)

# task
count = 0
for vowel in x:
    if vowel=='a'or vowel=='e'or vowel=='i'or vowel=='o'or vowel== 'u':
        count+=1
print(count)
# task done

if 'mother' in x:
    print('Available')
    
print('spam'*3)

# task
y = "I weigh 80 kilograms. He weighs 65 kilograms."
count=0
for letter in y:
    count+=1
    print(letter*count)
# task done

print(y.replace(y[2],"t"))
print(y.count('e'))

word = 'kilograms'
replacer = 'kg'
print(y.count(word))
print(y.replace(word, replacer))