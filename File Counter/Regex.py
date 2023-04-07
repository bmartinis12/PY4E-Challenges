import re

name = input("File Name: ")
try:
    fhandle = open(name)
except:
    print("Error opening:", name)
    quit()
numlist = list()
for line in fhandle:
    line = line.rstrip()
    extract = re.findall('([0-9]+)', line)
    for number in extract:
        num = float(number)
        numlist.append(num)
sum = int(sum(numlist))
print("Sum:", sum)
