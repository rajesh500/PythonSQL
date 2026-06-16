import json


# Encoding or Serialization:
#It is the process of converting python objects into a JSON formatted string.

# Decoding or Deserialization:
#It is the process of converting Json string back into a python object, typically dictinary.

# load --> file to json object
# loads --> JSON string to python object(dictionary)

# dump --> write json data to file
# dumps --> Python object into JSON string

# parse JSON from string

json_string = '{"name":"John", "age":30, "city":"New york"}'
data = json.loads(json_string)
print(data)
print(data['name'])



# parse JSON from a file

with open(r'Data\jsondata.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(data['name'])


# convert python objects to JSON Strings
data = {"name":"John", "age":30, "city":"New york"}
json_string = json.dumps(data)
print(json_string)




# writing json data to a file
data = {
"name": "John",
"age": 30,
"city": "New York"
}
with open(r'Data\data.json', 'w') as file:
    json.dump(data, file)



# Nested JSON Objects:     accessing nested json elements
json_string = '{"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "New York"}}'
data = json.loads(json_string)
print(data['age'])
print(data['address']['city'])


# JSON Array     accessing array elements
json_string = '{"name": "John", "age": 30, "skills": ["Python", "Django", "Machine Learning"]}'
data = json.loads(json_string)
print(data['skills'][0])




# adding element:
json_string = '{"model": "Model X", "year": 2022}'
json_data = json.loads(json_string)
print(json_data)
json_data['color'] = 'Red'  # Added
print(json_data)

del json_data['model']   # delete
print(json_data)

more_json_string = '{"model": "Model S", "color": "Red"}'
more_json_data = json.loads(more_json_string)
print(more_json_data)
json_data.update(more_json_data)  # update with two json object, not directly.
print(json_data)



# print(wjdata['data']['current_condition'][0]['temp_C'])