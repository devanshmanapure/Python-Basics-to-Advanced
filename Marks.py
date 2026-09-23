#Calculate total and percentage of 5 subjects
English = int(input("Enter Marks for English Subject"))
History = int(input("Enter Marks for History Subject"))
Science = int(input("Enter Marks for Science Subject"))
Maths = int(input("Enter Marks for Maths Subject"))
Sanskrit = int(input("Enter Marks for Sanskrit Subject"))

result1 = (English+History+Science+Maths+Sanskrit)
print("Total marks=", result1)
result2 = (result1)/5
print("Avg Makrs=", result2)
