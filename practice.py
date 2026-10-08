print("===== STUDENT RESULT =====")

name = input("Enter student name: ")

m1 = int(input("Enter Python marks: "))
m2 = int(input("Enter C++ marks: "))
m3 = int(input("Enter Java marks: "))
m4 = int(input("Enter DB marks: "))
m5 = int(input("Enter Web marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n===== RESULT =====")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")