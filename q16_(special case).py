#count chr without using count function and set from a str output in tuple

def count_chr(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return tuple(count.items())

# Example usage
input_str = "programming"
result = count_chr(input_str)
print(result)