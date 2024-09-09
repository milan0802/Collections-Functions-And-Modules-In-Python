"""How will you create a dictionary using tuples in python?"""

tup=((1,'A'),(2,"B"),(3,'C'))

d=dict((i,j) for i,j in tup)
print(d)
