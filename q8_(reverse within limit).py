l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))

L = []


for i in range(start):
    L.append(l[i])

for i in range(end, start - 1, -1):
    L.append(l[i])


#explanation
'''
    if the length of the modified list is not 
    equal to the original list, we need to 
    append the remaining elements of the original 
    list to the modified list.
    
    and if the modified length is equal to the 
    original list, we can stop appending the 
    remaining elements of the original list to 
    the modified list.
'''

if len(L) != len(l):
    for i in range(end, len(l)):
        L.append(l[i])

print("The modified list is:", L)