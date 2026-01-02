import requests

response = requests.get("https://jsonplaceholder.typicode.com/poss")
data = response.json()
code = response.status_code
print(code)
