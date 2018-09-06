import json


aName = input('Please enter your name: ')
data = {
   'name' : 'aName',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data)