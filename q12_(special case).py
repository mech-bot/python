l = [18,3,62,25,7,99,36,22]

count = 0
for i in range(len(l)):
    sum =0
    for j in range(i + 1, len(l)):
        sum += l[j]
    if l[i] > sum:
        count += 1
        print(i)

print("The number of elements that are greater than the sum of elements to their right is:", count)