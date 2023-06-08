import requests
# https://rahulshettyacademy.com
# 'visited-month'
cookie = {'visited-month' : 'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False,cookies=cookie,timeout=10)
print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visited-month' : 'February'})
re = se.get('https://httpbin.org/cookies', cookies={'visited-year': '2022'})
print(re.text)

# attachments

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
file = {'file': open('C:\\Users\\Sachin\\Desktop\\reap.png', 'rb')}
res = requests.post(url,files=file)
print(res.status_code)
print(res.text)
