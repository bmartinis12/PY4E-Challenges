from urllib.request import urlopen
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = int(input("Enter count: "))
position = int(input("Enter position: "))
finalUrl = None
while count > 0:
    tags = soup('a')
    alist = list()
    for tag in tags:
        alist.append(tag.get('href', None))
    newUrl = alist[position - 1]
    print("Retrieving:", newUrl)
    finalUrl = newUrl
    html = urlopen(newUrl, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    count = count - 1
