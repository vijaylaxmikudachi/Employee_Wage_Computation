import random

# Constants
WAGE_PER_HOUR = 20        # Wage per hour
FULL_DAY_HOURS = 8        # Full working hours for full-time
PART_TIME_HOURS = 4       # Working hours for part-time

# Function to calculate daily wage
def calculate_daily_wage():
    # Randomly choose between absent (0), part-time (1), or full-time (2)
    attendance = random.randint(0, 2)
    
    if attendance == 2:
        # Employee is present for full-time
        daily_wage = WAGE_PER_HOUR * FULL_DAY_HOURS
        print(f"Employee is Full-time. Daily Wage: ${daily_wage}")
    elif attendance == 1:
        # Employee is present for part-time
        daily_wage = WAGE_PER_HOUR * PART_TIME_HOURS
        print(f"Employee is Part-time. Daily Wage: ${daily_wage}")
    else:
        # Employee is absent
        print("Employee is Absent. No Wage for today.")

# Calculate daily wage
calculate_daily_wage()
