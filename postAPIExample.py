
import requests
from datapayload import *
from utilities.configuration import *
from utilities.resources import *


url = getConfig()['API']['endpoint']+ ApiResources.addBook
header = {"Content-Type": "application/json"}
query = 'select * from Books'
addbook_response = requests.post(url, json=buildPayLoadFromDB(query), headers=header,)

print(addbook_response.json())
response_json = addbook_response.json()
print(type(addbook_response.json()))
bookId = response_json['ID']
print(bookId)

# Delete book
url_delete = getConfig()['API']['endpoint']+ ApiResources.deleteBook
response_deletebook = requests.post(url_delete,json={'ID': bookId},headers=header, )
assert response_deletebook.status_code == 200
res_json = response_deletebook.json()

print(res_json['msg'])
assert res_json['msg'] == "book is successfully deleted"

se = requests.session()
se.auth = auth=('saching123473@gmail.com', getPassword())
url = "https://api.github.com/user"
github_response = se.get(url)
print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)