#Inverted pyramid
a = int(input("Enter a Value"))
for i in range(a, 0, -1):
    print(" " * (a - i)+ "*" * (2*i-1))
