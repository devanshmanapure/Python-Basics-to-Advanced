input1=int(input("Enter a number"))
sum=0
sum1=0
temp=input1
str1=str(temp)

while input1!=0:
        rem=input1%10
        sum1=sum1+rem
        input1=input1//10

print(f"The input was {temp} and the sum is {sum1}")
print(f"total numer of digits in {temp} are {len(str1)}")
