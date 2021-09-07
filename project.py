import csv
import math

with open("data.csv",newline="")as f:
    reader=csv.reader(f)
    file=list(reader)

data=file[0]


total=0
n=len(data)
for i in data:
    total=total+int(i)

mean=total/n 
print(mean)
squared=[]

for i in data:
    a=int(i)-mean
    a=a**2
    squared.append(a)

print(squared)

add=0
for i in squared:
    add=add+i 

print(add)

result=add/(len(data)-1)

print(result)

standarddeviation=math.sqrt(result)
print(standarddeviation)