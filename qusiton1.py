def find_unique_number(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a
result = find_unique_number(2, 2, 3)
print("The number that occurs exactly once is:", result)