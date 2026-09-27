#Print multiplication table
a = int(input("Enter a number"))
for i in range(1,10+1):
    result = a*i
    print(a, "*", i, "=", result)
