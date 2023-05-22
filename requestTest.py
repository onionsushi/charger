import requests

r = requests.get("http://[2607:fea8:1f1c:6600::12]:8000/")
print(r.text)