import json

data = '''{
    "name": "Chuck",
    "phone":{
        "type":"int1",
        "number":"+1734 303 4456"
     },    
     "email":{
        "hide":"yes"
     }
 }'''

info = json.loads(data)
print(info)
print('Name:',info['name'])
print('Hide:',info['email']['hide'])

input = '''[
    {"id":"001",
     "x":"2",
     "name":"Chuck"
    },
    {"id":"009",
     "x":"7",
     "name":"Chuck"
    }
]'''

v = json.loads(input)
print("User count", len(v))
for item in v:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])