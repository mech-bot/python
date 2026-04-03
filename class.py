class temp:
    'ok'
    c = 0
    __n = int()
    
    def __init__(self,n):
        self.__n = n
    def print_(self):
        print(self.__n)
        
        
    def update(self):
        self.__n +=1
    

a = temp(10)
b = temp(20)
a.update()

# print(a.__n) does accesible because private data member cannot be accessed outside the class
a.print_()
b.print_()

print(temp.__doc__)
print(temp.__dict__)
print(temp.__name__)
print(temp.__module__)
print(temp.__bases__)