import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter JSON data: ")
data = urllib.request.urlopen(url, context=ctx).read().decode()
jsonread = json.loads(data)

sum = 0
for item in jsonread['comments']:
    num = item['count']
    sum = sum + num
print("Sum:", sum)
