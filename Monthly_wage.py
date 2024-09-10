import random

# Constants
WAGE_PER_HOUR = 20        # Wage per hour
FULL_DAY_HOURS = 8        # Full working hours for full-time
PART_TIME_HOURS = 4       # Working hours for part-time
WORKING_DAYS_PER_MONTH = 20  # Total working days in a month

# Function to calculate wages for the month
def calculate_monthly_wage():
    total_wage = 0

    for day in range(1, WORKING_DAYS_PER_MONTH + 1):
        # Randomly choose between absent (0), part-time (1), or full-time (2)
        attendance = random.randint(0, 2)
        
        if attendance == 2:
            # Full-time employee
            daily_wage = WAGE_PER_HOUR * FULL_DAY_HOURS
            print(f"Day {day}: Employee is Full-time. Daily Wage: ${daily_wage}")
        elif attendance == 1:
            # Part-time employee
            daily_wage = WAGE_PER_HOUR * PART_TIME_HOURS
            print(f"Day {day}: Employee is Part-time. Daily Wage: ${daily_wage}")
        else:
            # Employee is absent
            daily_wage = 0
            print(f"Day {day}: Employee is Absent. No Wage for today.")

        # Add the daily wage to total monthly wage
        total_wage += daily_wage
    
    print(f"\nTotal Wage for the Month: ${total_wage}")

# Calculate monthly wage
calculate_monthly_wage()
