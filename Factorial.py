#Find factorial of N
n = int(input("Enter a number n"))
result = 1
for i in range(1,n+1):
    result = result*i
    print("Factorial of this number is", result)
