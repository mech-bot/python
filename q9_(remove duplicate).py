l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
'''
set contains only unique elements, so we 
can convert the list to a set and then 
back to a list to remove duplicates.
'''

L = list(set(l))
print("The list after removing duplicates is:", L)