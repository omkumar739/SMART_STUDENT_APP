import os

def main_menu():
    while True:
        print("\n--- Smart Campus System ---")
        print("1. Registration | 2. Enrollment | 3. Records | 4. Search/Sort | 5. Fee | 6. File Mgmt | 7. Scan | 8. Analytics | 9. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            exec(open("student_registration.py").read()) # Runs Lab 1 code
        elif choice == '2':
            exec(open("course_enrollment.py").read())    # Runs Lab 2 code
        elif choice == '3':
            exec(open("student_records.py").read())      # Runs Lab 3 code
        elif choice == '4':
            exec(open("search_sort_students.py").read()) # Runs Lab 4 code
        elif choice == '5':
            exec(open("fee_calculation.py").read())      # Runs Lab 5 code
        elif choice == '6':
            exec(open("file_manager.py").read())         # Runs Lab 6 code
        elif choice == '7':
            exec(open("directory_scanner.py").read())    # Runs Lab 7 code
        elif choice == '8':
            exec(open("performance_analytics.py").read())# Runs Lab 8 code
        elif choice == '9':
            print("Exiting system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()