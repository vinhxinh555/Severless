import requests

url = "https://solitary-meadow-dc0f.long73365.workers.dev/"
params = {"name": "test"}

res = requests.get(url, params=params)
print(res.json())
print(res.json())