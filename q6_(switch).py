age = int(input("Enter your age: "))

"""
   for switch case we have to write for each 
   case and we can use match(<var>) to check the age 
   in that range
"""
match age:
    case i if i in range(0, 6):
        print("bus fare is free")
    case i if i in range(5, 13):
        print("bus fare is 50rs")
    case i if i in range(12, 60):
        print("bus fare is 100rs")
    case i if i in range(59, 200):
        print("bus fare is 40rs")

#for original code we have to write if else statement for each case
"""
if age<5:
    print("bus fare is free")
elif age>=5 and age<13:
    print("bus fare is 50rs")
elif age>=12 and age<60:
    print("bus fare is 100rs")
elif age>=59 and age<200:
    print("bus fare is 40rs")
"""

#check for invalid age
if age < 0 or age > 200:
    print("invalid age")
    
