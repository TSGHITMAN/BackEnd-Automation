import json

courses = '{"name" : "Sachin" , "languages" : ["java" , "python"]}'

# loads method json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

list_language = dict_courses['languages']
print(type(list_language))
print(list_language[0])

# parse the content from json file

with open('C:\\Users\\Sachin\\Desktop\\jsonfile.json') as f:
    data = json.load(f)
    print((type(data)))
    print(data)
    print(data['courses'][1]['title'])

