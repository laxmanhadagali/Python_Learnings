Stud_name=input("Enter Name of Student ")
python=int(input("Enter Subject1 Marks " ))
HTML=int(input("Enter Subject2 Marks "))
DAA=int(input("Enter Subject3 Marks "))
WCMS=int(input("Enter Subject4 Marks "))
IC=int(input("Enter Subject5 Marks "))
print("\n")
print("STUDENT MARKSHEET")
print(f"Name:",Stud_name)
print(f"python:",python)
print(f"HTML:",HTML)
print(f"DAA:",DAA)
print(f"WCMS:",WCMS)
print(f"IC:",IC)


total=python+HTML+DAA+WCMS+IC
print(f"Total marks is:",total)

average=total/5
print(f"average is:",average)

