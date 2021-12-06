import csv
f=open('C:\\Users\\Lenovo\\Desktop\\data.csv','r')
reader=csv.reader(f)
next(reader)
for i in reader:
    print(i)
