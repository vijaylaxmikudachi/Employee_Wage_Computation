import random

# Function to check attendance
def check_attendance():
    # Generate random number: 0 for absent, 1 for present
    attendance = random.randint(0, 1)
    
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")

# Check attendance
check_attendance()
