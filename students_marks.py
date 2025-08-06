student_marks = {"Alice":84 , "Bob":90 , "Charlie":70 , "David":60 , "Eve":50 }
try:
    student = input("Enter the student's name: ")
    if student.capitalize() in student_marks:
        student = student.capitalize()

    print(f"{student}'s marks: {student_marks[student]}")
except :
    print("student not found")