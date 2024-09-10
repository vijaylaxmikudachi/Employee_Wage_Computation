import random

# Constants
WAGE_PER_HOUR = 20  # Wage per hour
FULL_DAY_HOURS = 8  # Full working hours in a day

# Function to calculate daily wage
def calculate_daily_wage():
    # Generate random attendance (1 for present, 0 for absent)
    attendance = random.randint(0, 1)
    
    if attendance == 1:
        # Employee is present
        daily_wage = WAGE_PER_HOUR * FULL_DAY_HOURS
        print(f"Employee is Present. Daily Wage: ${daily_wage}")
    else:
        # Employee is absent
        print("Employee is Absent. No Wage for today.")

# Calculate daily wage
calculate_daily_wage()
