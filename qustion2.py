def most_frequent_letter(s):
    count_a = s.count('A')
    count_b = s.count('B')
    
    if count_a > count_b:
        return 'A'
    elif count_b > count_a:
        return 'B'
    else:
        return 'EQUAL'
string = input("Enter A & B ")
result = most_frequent_letter(string)
print("The most frequent letter is:", result)
