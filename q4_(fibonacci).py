def print_fibonacci():
    n = int(input("enter number of terms:"))
    
    c1 =0
    c2 =1
    count = 0
    if n <= 0:
        print("Please enter a positive integer.")
    
    print(c1,end=" ")
    print(c2,end=" ")
    
    while count < n-2:
        c3 = c1 + c2
        print(c3,end=" ")
        c1 = c2
        c2 = c3
        count += 1
print_fibonacci()