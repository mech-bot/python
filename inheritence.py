class parent:
    c = int()
    def __init__(self,n,m):
        print("This is parent class created")
        self.c = n
        super().__init__(m) # this will call the parent2 class constructor
    
    def parent_method(self):
        print("This is parent method")
        self.c += 1
        
class parent2:
    d = int()
    def __init__(self,m):
        print("This is parent2 class created")
        self.d = m

class child(parent, parent2):
    def __init__(self,n,m):
        super().__init__(n,m) # this will call the parent class constructor
        # super().__init__(m) # this will call the parent2 class constructor
        print("This is child class created")
        
a = child(23, 45)
# b = parent(10)
# print(a.c)
# a.parent_method()
# print(child.__bases__)
# print(isinstance(b, child))

print(a.c, a.d)
print(child.__mro__)

