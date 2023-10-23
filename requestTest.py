import requests

# r = requests.get("http://10.0.0.176:8000/locktoggle")
r = requests.get("http://10.0.0.176:8000/")
print(r.text)