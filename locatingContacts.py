import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
   'number': ['1234', '5678', '2222', '1111', '0909']
}
contact = pd.DataFrame(data, index=data['name'])
print(contact)
nm = 'James'
print(contact.loc[nm])