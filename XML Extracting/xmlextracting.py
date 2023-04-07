import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter XML data: ')
data = urllib.request.urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

sum = 0

for item in counts:
    print(item)
    num = item.text
    num = int(num)
    sum = sum + num
print("Sum:", sum)
