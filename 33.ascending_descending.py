""""Write a Python script to sort (ascending and descending) a dictionary by 
value."""

import operator
d={1:0,5:3,4:2,7:1,2:5,3:4}

abc_d=dict(sorted(d.items(),key=operator.itemgetter(1)))
defg_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))

print("ascending:",abc_d)
print("descending:",defg_d)
