#Check whether a number is prime
a = int(input("Enter a number"))
for i in range (2,a):
    if a%i==0:
        print(a, "The number is not prime")
        break
else:
    print(a, "The number is prime")
