import random

# Constants
WAGE_PER_HOUR = 20        # Wage per hour
FULL_DAY_HOURS = 8        # Full working hours for full-time
PART_TIME_HOURS = 4       # Working hours for part-time

# Function to calculate daily wage using switch-case equivalent
def calculate_daily_wage():
    # Randomly choose between absent (0), part-time (1), or full-time (2)
    attendance = random.randint(0, 2)
    
    # Switch-case equivalent using a dictionary
    switcher = {
        0: lambda: "Employee is Absent. No Wage for today.",
        1: lambda: f"Employee is Part-time. Daily Wage: ${WAGE_PER_HOUR * PART_TIME_HOURS}",
        2: lambda: f"Employee is Full-time. Daily Wage: ${WAGE_PER_HOUR * FULL_DAY_HOURS}"
    }
    
    # Execute the case
    print(switcher.get(attendance, lambda: "Invalid attendance")())

# Calculate daily wage
calculate_daily_wage()
