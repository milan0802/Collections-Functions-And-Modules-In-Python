"""Write a Python program to find the second smallest number in a list."""
l=[1,3,5,8,9,4,10,16,18,13]

smallest=l[0]
second_small=l[5]

for i in l:
    if i<smallest:
        second_small=smallest
        smallest=i
    elif i<second_small and i!=smallest:
        second_small=i
print(smallest)
print(second_small)

