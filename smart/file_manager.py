# Updated file_manager.py to align with Analytics requirements
new_name = input("Enter Student Name: ")
math = input("Enter Math Marks: ")
science = input("Enter Science Marks: ")
english = input("Enter English Marks: ")

# 'a' mode appends to the file
with open("student_performance.csv", "a") as file:  
    file.write(f"{new_name},{math},{science},{english}\n")
    print("Record added successfully to student_performance.csv!")