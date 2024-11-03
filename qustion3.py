def find_largest_number():
    n = int(input("Enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    largest = max(numbers)
    return largest
largest_number = find_largest_number()
print("The largest number is:", largest_number)
