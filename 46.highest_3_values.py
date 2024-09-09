""" Write a Python program to find the highest 3 values in a dictionary"""

d={'a':13,'b':65,'c':12,'d':48}

values=list(d.values())

values.sort(reverse=True)

print(values[:3])
