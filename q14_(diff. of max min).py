t = (5, 10, 3, 8, 15)

max_ = 0
min_ = t[0]
for i in t:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
print("The difference between the maximum and minimum values is:", max_ - min_)