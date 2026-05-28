# Student Fee Calculation
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee

tuition = int(input("Enter Your Tution Fee:"))
hostel = int(input("Enter Your Hostel Fee if applicable:"))
transport =int(input("Enter Your Transport Fee If applicable:"))
print("Total Fee:", calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport))