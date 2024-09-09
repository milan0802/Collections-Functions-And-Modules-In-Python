"""Write a Python program to convert a list of tuples into a dictionary."""

l=[('a',1),('b',2),('c',3)]

d={}

for i,j in l:
    d.setdefault(i,[]).append(j)
print(d)
