l = [1, 2, 3, 4, 5]
target = 5
L = []

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            L.append((l[i], l[j]))

print("The pairs of elements that sum up to the target are:", L)