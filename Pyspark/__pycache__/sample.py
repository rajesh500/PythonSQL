string_variable = "example"
string_variable = "'" + string_variable + "'"
print(string_variable)  # Output: 'example'

name = "Bob"
job = "engineer"
print("My name is {} and I am an {}.".format(name, job))
print("My name is {0} and I am an {1} and i have a '{0}'.".format(name, job))
print("My name is {name} and I am an {job}.".format(name=name, job=job))