contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}
#your code goes here
name = input()
if name in contacts:
    print(contacts[name][1])
else:
    print ('Not found')
    
    # tuples
