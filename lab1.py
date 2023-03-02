import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime
x = input("Give URL: " )
r = requests.get(x)
for i in r.headers:
    print(i);




