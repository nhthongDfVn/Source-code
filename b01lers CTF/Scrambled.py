import requests
import urllib.parse
def mysplit(s):
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    return head, tail
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1  
session = requests.Session()
my_list = [' ']*150
i=0
while True:
    i=i+1
    response = session.get('http://web.ctf.b01lers.com:1002/')
    s=session.cookies.get_dict()['transmissions']
    if i>1:
        m=mysplit(s.split('kxkxkxkxsh')[1])
        if m[1]!='':
            my_list[int(m[1])]=m[0]
            print(urllib.parse.unquote(listToString(my_list))[::2])
        
