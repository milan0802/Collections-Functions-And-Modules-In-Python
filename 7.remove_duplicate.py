"""Write a Python program to remove duplicates from a list."""
l=[]
a=[1,2,3,1,2,3]

for i in a:
    if i not in l:
        l.append(i)
print(l)

