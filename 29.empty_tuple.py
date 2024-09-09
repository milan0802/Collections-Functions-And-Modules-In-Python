""" Write a Python program to remove an empty tuple(s) from a list of tuples."""

tup=[(4,5,6),(7,8,9),()]
tup=[i for i in tup if i!=()]
print(tup)
