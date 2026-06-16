import requests

response = requests.get('https://data.fixer.io/api/latest')
data = response.json()   # data display into dictionary objects
print(data)