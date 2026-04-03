l = [1, 2, 2, 3, 4, 4]
L = []

for i in l:
    c = l.count(i)
    if (i, c) not in L:
        L.append((i, c))
        
print("The frequency of each element in the list is:", L)