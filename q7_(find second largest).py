l = [5, 2, 8, 1, 9, 9]

'''
if there are duplicate largest numbers, 
we give the second largest number as the 
largest number. For example, in the list 
[5, 2, 8, 1, 9, 9], the largest number is 9
and the second largest number is also 9.

if l = [5, 2, 8, 1, 9, 3], the largest number 
is 9 and the second largest number is 8.
'''


max_num = 0
for i in l:
    if i > max_num:
        max_num = i

print("The largest number is:", max_num)
second_largest = 0
for i in l:
    if i > second_largest and i <= max_num:
        second_largest = i

print("The second largest number is:", second_largest)