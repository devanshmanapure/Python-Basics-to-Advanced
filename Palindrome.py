input1 = int(input("Enter a number to reverse"))
rem = 0
rev = 0
temp = input1 
while input1 != 0:
    rem = input1 % 10
    rev = rev * 10 + rem
    input1 = input1 // 10
print(rev)
if temp == rev:
    print("palindrome")
else:
        print("not palindrome")
