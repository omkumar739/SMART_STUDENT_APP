# Sorting and Searching Student IDs
student_ids = [105, 102, 110, 108, 101, 115]
# Bubble Sort
n = len(student_ids)
for i in range(n):
    for j in range(0, n-i-1):
        if student_ids[j] > student_ids[j+1]:
            student_ids[j], student_ids[j+1] = student_ids[j+1], student_ids[j]
print("Sorted IDs (Bubble Sort):", student_ids)

# Linear Search
target = int(input("enter the id to search:"))
found_index = -1
for i in range(len(student_ids)):
    if student_ids[i] == target:
        found_index = i
        break
if found_index != -1:
    print("Linear Search: ID", target, "found at index", found_index)