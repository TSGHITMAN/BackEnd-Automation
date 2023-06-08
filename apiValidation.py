import json
import requests
from utilities.configuration import *
from utilities.resources import *

url = getConfig()['API']['endpoint']+ ApiResources.getBook
header = {"Content-Type": "application/json"}
response = requests.get(url,params= {'AuthorName': 'Rahul Shetty2'},)

print(type(response.text))
print(response.text)

# first approach

dict_response = json.loads(response.text)
print(type(dict_response))
print(dict_response[0]['isbn'])
# second approach

json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])

assert dict_response == json_response
assert response.status_code == 200
print(response.status_code)
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# retrieve the book details with isbn RGHCC

for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        break
expectedBook = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '22755'}

assert actualBook == expectedBook
