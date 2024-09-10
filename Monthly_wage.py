import random

# Constants
WAGE_PER_HOUR = 20        # Wage per hour
FULL_DAY_HOURS = 8        # Full working hours for full-time
PART_TIME_HOURS = 4       # Working hours for part-time
MAX_WORKING_DAYS = 20     # Maximum working days per month
MAX_WORKING_HOURS = 100   # Maximum working hours per month

# Function to calculate wages for the month
def calculate_wage_till_condition():
    total_working_days = 0
    total_working_hours = 0
    total_wage = 0
    
    # Loop until total working days or total working hours reach their limits
    while total_working_days < MAX_WORKING_DAYS and total_working_hours < MAX_WORKING_HOURS:
        # Randomly choose between absent (0), part-time (1), or full-time (2)
        attendance = random.randint(0, 2)
        
        if attendance == 2:
            # Full-time employee
            hours_worked = FULL_DAY_HOURS
            print(f"Day {total_working_days + 1}: Employee is Full-time. Worked {hours_worked} hours.")
        elif attendance == 1:
            # Part-time employee
            hours_worked = PART_TIME_HOURS
            print(f"Day {total_working_days + 1}: Employee is Part-time. Worked {hours_worked} hours.")
        else:
            # Employee is absent
            hours_worked = 0
            print(f"Day {total_working_days + 1}: Employee is Absent.")
        
        # Update the total working hours and days
        total_working_hours += hours_worked
        if hours_worked > 0:
            total_working_days += 1
        
        # Calculate daily wage and add to the total wage
        daily_wage = WAGE_PER_HOUR * hours_worked
        total_wage += daily_wage

        # Check if total hours have reached the limit
        if total_working_hours >= MAX_WORKING_HOURS:
            print(f"\nReached the maximum of {MAX_WORKING_HOURS} working hours.")
            break
        elif total_working_days >= MAX_WORKING_DAYS:
            print(f"\nReached the maximum of {MAX_WORKING_DAYS} working days.")
            break

    print(f"\nTotal Working Days: {total_working_days}")
    print(f"Total Working Hours: {total_working_hours}")
    print(f"Total Wage for the Month: ${total_wage}")

# Calculate the wage till the condition is met
calculate_wage_till_condition()
