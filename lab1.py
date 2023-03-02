import requests  # εισαγωγή της βιβλιοθήκης
import requests
from datetime import datetime;
x = input("Enter URL: ")
r = requests.get(x)
print("\nHeaders: \n")
for i in r.headers :
    print (i)
print("\nServer: " + r.headers['Server'])
if('Set-Cookie'in r.headers):
    print("\nThe URL Cookies: \n")
    for j in r.cookies:
        print(j.name)
        if j.expires==None:
            print("Does Not Expire\n")
        else:
            e=float(j.expires)
            n=datetime.now().timestamp()
            print(" Expires In: ")
            print(datetime.fromtimestamp(e)-datetime.fromtimestamp(d))
            print("\n")
else:
    print("No Cookie")



