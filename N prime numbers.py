# Print prime numbers from 1-N
a = int(input("Enter a number: "))
for i in range(2, a + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)
