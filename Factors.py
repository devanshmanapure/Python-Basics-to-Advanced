input1=int(input("Enter a number to print Factors:"))
for i in range(1,input1+1):
    if input1%i==0:
        print(f" {i} is a Factor of {input1}")
    else:
        continue
