def average_of_numbers(M, N):
    if M > N:
        M, N = N, M 
    total_sum = sum(range(M, N+1))
    count = N - M + 1
    average = total_sum / count
    return average
M = int(input("Enter M: "))
N = int(input("Enter N: "))
result = average_of_numbers(M, N)
print("Average of numbers from", M, "to", N, "is:", result)