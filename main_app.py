import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# GLOBAL DATABASE & CUSTOM EXCEPTIONS
# ==========================================
students_db = []
student_id_counter = 101

# Custom exception for Lab 7
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

# ==========================================
# LAB 1: Registration & Grade Evaluation
# ==========================================
def register_student():
    global student_id_counter
    print("\n--- Student Registration ---")
    name = input("Enter student name: ").strip()
    
    # Collecting specific subject marks to integrate with Lab 8 Analytics
    try:
        math = float(input("Enter Math score (0-100): "))
        science = float(input("Enter Science score (0-100): "))
        english = float(input("Enter English score (0-100): "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    avg_score = round((math + science + english) / 3, 2)
    
    # Grade evaluation using conditional statements
    if 90 <= avg_score <= 100:
        grade, remark = "A", "Excellent"
    elif avg_score >= 75:
        grade, remark = "B", "Very Good"
    elif avg_score >= 60:
        grade, remark = "C", "Good"
    elif avg_score >= 40:
        grade, remark = "D", "Average"
    else:
        grade, remark = "F", "Needs Improvement"
        
    student_record = {
        "id": student_id_counter,
        "name": name,
        "math": math,
        "science": science,
        "english": english,
        "avg_score": avg_score,
        "grade": grade,
        "remark": remark,
        "courses": []
    }
    
    students_db.append(student_record)
    print(f"\nStudent {name} registered successfully with ID {student_id_counter}!")
    print(f"Average Score: {avg_score} | Grade: {grade} | Remark: {remark}")
    student_id_counter += 1

# ==========================================
# LAB 2: Course Enrollment Management
# ==========================================
def enroll_courses():
    print("\n--- Course Enrollment ---")
    if not students_db:
        print("No students registered yet!")
        return
        
    try:
        s_id = int(input("Enter Student ID to enroll: "))
    except ValueError:
        print("Invalid ID.")
        return

    student = next((s for s in students_db if s["id"] == s_id), None)
    if not student:
        print("Student not found.")
        return

    max_courses = 5
    print(f"Enrolling courses for {student['name']}. Maximum 5 courses allowed.")
    
    # Loop for multiple entries
    while True:
        if len(student["courses"]) >= max_courses:
            print("Maximum course limit reached!")
            break
            
        course_name = input("Enter course name (or 'done' to finish): ").strip()
        if course_name.lower() == 'done':
            break
            
        credits_input = input("Enter credit value: ").strip()
        
        # Validation
        if not credits_input.isdigit() or int(credits_input) <= 0:
            print("Invalid credit value! Must be a positive integer. Skipping entry...")
            continue
            
        student["courses"].append((course_name, int(credits_input)))
        print(f"Course '{course_name}' added.")
        
    print(f"\nTotal courses enrolled for {student['name']}: {len(student['courses'])}")

# ==========================================
# LAB 3: Event Participation (Sets)
# ==========================================
def event_participation():
    print("\n--- Event Participation Analysis ---")
    # Hardcoded sets as per the lab manual for demonstration
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    common = event_A & event_B
    all_participants = event_A | event_B
    only_a = event_A - event_B
    
    print(f"Event A Participants: {event_A}")
    print(f"Event B Participants: {event_B}")
    print(f"Common Participants (Intersection): {common}")
    print(f"All Participants (Union): {all_participants}")
    print(f"Only Event A (Difference): {only_a}")

# ==========================================
# LAB 4: Sorting and Searching (Bubble Sort & Binary Search)
# ==========================================
def sort_and_search_ids():
    print("\n--- Sorting and Searching Student IDs ---")
    if not students_db:
        print("No students registered. Please add students first.")
        return
        
    # Extract IDs from the global database
    ids = [s["id"] for s in students_db]
    print(f"Original IDs: {ids}")
    
    # Bubble Sort
    n = len(ids)
    for i in range(n):
        for j in range(0, n-i-1):
            if ids[j] > ids[j+1]:
                ids[j], ids[j+1] = ids[j+1], ids[j] # Pythonic swap
                
    print(f"Sorted IDs (Bubble Sort): {ids}")
    
    # Binary Search
    try:
        target = int(input("Enter ID to search using Binary Search: "))
    except ValueError:
        print("Invalid ID.")
        return
        
    low, high = 0, len(ids) - 1
    found_index = -1
    
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            found_index = mid
            break
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    if found_index != -1:
        print(f"Binary Search: ID {target} found at sorted index {found_index}.")
    else:
        print(f"Binary Search: ID {target} not found.")

# ==========================================
# LAB 5: Fee Calculation (Functions)
# ==========================================
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee

def fee_menu():
    print("\n--- Fee Calculation ---")
    try:
        t_fee = float(input("Enter Tuition Fee: "))
        h_fee = float(input("Enter Hostel Fee (Enter 0 if none): "))
        tr_fee = float(input("Enter Transportation Fee (Enter 0 if none): "))
        
        total = calculate_fee(t_fee, h_fee, tr_fee)
        print(f"Total Calculated Fee: ₹{total}")
    except ValueError:
        print("Invalid input! Please enter numbers.")

# ==========================================
# LAB 6: File Handling
# ==========================================
def file_handling():
    print("\n--- File Handling ---")
    if not students_db:
        print("No records to save.")
        return
        
    filename = "student_records.txt"
    
    # Write to file
    with open(filename, "w") as file:
        file.write("ID,Name,Avg_Marks\n")
        for s in students_db:
            file.write(f"{s['id']},{s['name']},{s['avg_score']}\n")
    print(f"Records successfully written to {filename}.")
    
    # Read and Process
    print("\nGenerating Report from File:")
    total_students, total_marks, highest_marks = 0, 0, -1
    top_student = ""
    
    with open(filename, "r") as file:
        records = file.readlines()
        for record in records[1:]: # Skip header
            parts = record.strip().split(",")
            marks = float(parts[2])
            
            total_students += 1
            total_marks += marks
            
            if marks > highest_marks:
                highest_marks = marks
                top_student = parts[1]
                
    if total_students > 0:
        print(f"Total Students: {total_students}")
        print(f"Average System Marks: {total_marks / total_students:.2f}")
        print(f"Top Student: {top_student} with {highest_marks} marks")

# ==========================================
# LAB 7: Directory Scanner
# ==========================================
def directory_scanner():
    print("\n--- Directory Scanner ---")
    path = input("Enter directory path to scan (or press Enter for current): ").strip()
    if path == "": path = "."
    
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")
            
        print(f"\nScanning directory: {path}\n")
        is_empty = True
        
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            
            for f in files:
                print(f"{sub_indent}{f}")
                is_empty = False
                
        if is_empty:
            raise MissingFileOrFolderError(f"Empty folder detected: {path}")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# ==========================================
# LAB 8: Performance Analysis (Pandas/NumPy/Plt)
# ==========================================
def performance_analytics():
    print("\n--- Performance Analytics ---")
    if not students_db:
        print("No student data available! Please register students first.")
        return
        
    # 1. Dynamically create the CSV from our global database
    csv_filename = "student_performance.csv"
    try:
        df = pd.DataFrame([{
            'Name': s['name'], 
            'Math': s['math'], 
            'Science': s['science'], 
            'English': s['english']
        } for s in students_db])
        
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to {csv_filename}")
        
        # 2. Read and analyze
        df = pd.read_csv(csv_filename)
        print("\n--- Statistical Summary (Pandas) ---")
        print(df.describe())
        
        # 3. NumPy Operations
        scores = df[["Math", "Science", "English"]].to_numpy()
        mean_scores = np.mean(scores, axis=0)
        
        print("\n--- NumPy Analysis ---")
        print(f"Mean Scores (Math, Science, English): {mean_scores}")
        
        # 4. Top Performers
        print("\n--- Top Performers ---")
        print(f"Math: {df.loc[df['Math'].idxmax(), 'Name']}")
        print(f"Science: {df.loc[df['Science'].idxmax(), 'Name']}")
        print(f"English: {df.loc[df['English'].idxmax(), 'Name']}")
        
        # 5. Visualizations
        print("\nGenerating charts... (Close the chart windows to continue)")
        
        # Chart 1: Averages
        plt.figure(figsize=(6, 4))
        plt.bar(["Math", "Science", "English"], mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.show()
        
        # Chart 2: Student Comparison
        df.plot(x="Name", y=["Math", "Science", "English"], kind="bar", figsize=(8, 5))
        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")
        plt.xticks(rotation=0)
        plt.show()

    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# ==========================================
# LAB 9 & 10: MAIN DASHBOARD
# ==========================================
def main_dashboard():
    while True:
        print("\n" + "="*50)
        print("   SMART CAMPUS INFORMATION SYSTEM DASHBOARD   ")
        print("="*50)
        print("1. Register Student & Evaluate Grade (Lab 1)")
        print("2. Course Enrollment (Lab 2)")
        print("3. Event Participation Analysis (Lab 3)")
        print("4. Search & Sort Student IDs (Lab 4)")
        print("5. Calculate Fees (Lab 5)")
        print("6. File Manager - Save/Report (Lab 6)")
        print("7. Directory Scanner (Lab 7)")
        print("8. Performance Analytics (Lab 8)")
        print("9. Exit Application")
        print("="*50)
        
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1': register_student()
        elif choice == '2': enroll_courses()
        elif choice == '3': event_participation()
        elif choice == '4': sort_and_search_ids()
        elif choice == '5': fee_menu()
        elif choice == '6': file_handling()
        elif choice == '7': directory_scanner()
        elif choice == '8': performance_analytics()
        elif choice == '9':
            print("Exiting Smart Campus Information System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid number.")

if __name__ == "__main__":
    main_dashboard()