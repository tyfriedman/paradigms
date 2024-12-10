# tester.py
import requests

r = requests.get("http://student05.cse.nd.edu:51020/name/")
cont = r.content.decode()
print(cont)