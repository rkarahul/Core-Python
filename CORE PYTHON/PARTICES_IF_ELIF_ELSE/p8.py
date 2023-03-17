# Write a program to accept percentage fron the user and display the grade according to the following criteria
marks = int(input("Enter the Marks"))
if (marks>90):
    print("Grade is A")
elif(marks > 80 and marks <= 90):
    print("grade is B")
elif(marks >=60 and marks <=80):
    print("Grade is C")
elif(marks<60):
    print("Grade is D")

    