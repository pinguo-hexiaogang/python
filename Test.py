import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
bytes = response.read()
reponseStr = bytes.decode("utf8")
response.close()
print(reponseStr)