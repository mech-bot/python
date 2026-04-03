class one:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a
class two:
    def __init__(self, a):
        self.a = a

    # def __add__(self, other):
    #     return self.a + other.a
# Example usage:
obj1 = one(5)
obj2 = two(10.8)
result = obj1 + obj2
print(result)  # Output: 15