"""Write a Python program to unzip a list of tuples into individual lists."""

list1=[(1,2),(4,5),(10,12)]

list2=[i for i,j in list1]
list3=[j for i,j in list1]

print(list2)
print(list3)
