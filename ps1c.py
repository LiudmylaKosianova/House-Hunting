"""
The programm calculates optimal percentage of the salary to be saved every months for the user, 
if they want to save up for the downpayment in 36 months.
User's salary and the price of a house is taken as an input. 
The programm assumes, that
- the user gets the pay raise of 7% every six month
- the user's investments get annual return of 4%
- the downpayment amount is 25% of the house price
"""

annual_salary = 0.0 # user's annual salary will be entered by the user
total_cost = 0.0 #cost of a house will be entered by the user
down_payment = total_cost * 0.25 #the amount of money the user needs for downpayment 
monthly_salary = 0.0 #will be calculated after user gives input


user_input = input("Enter your annual salary: ")
annual_salary = float(user_input)
monthly_salary = annual_salary / 12
print("Your monthly salary is: ", monthly_salary)

user_input = input("Enter the cost of your dream home: ")
total_cost = float(user_input)
down_payment = total_cost * 0.25

def calc_months (down_payment,monthly_salary,portion_to_save):
    down_payment = down_payment
    monthly_salary = monthly_salary
    portion_to_save = portion_to_save

    count = 0
    current_savings = 0.0
    base = portion_to_save * monthly_salary  

    while down_payment > current_savings:
        current_savings += (current_savings * (0.4/12)) + base
        count += 1
        if count%6 == 0:
            monthly_salary += monthly_salary*0.7
            base = portion_to_save * monthly_salary

    return count


def calc_portion (a,b):
    down_payment = a
    monthly_salary = b

    portion_list = sorted(range(1,101))#create a sorted list in range 1-100 representing percents
    low = 0 #index for searching in the list
    high = len(portion_list) - 1 #index for searching in the list

    while low <= high:
        mid = (low + high) // 2 

        portion_to_save = portion_list[mid] / 100
        N_months = calc_months(down_payment,monthly_salary,portion_to_save)
        print("/t number of months is ...", N_months)

        if N_months == 36:
            return portion_to_save
        elif N_months > 36:
            low = mid + 1
        else:
            high = mid - 1
    return -1

portion = calc_portion (down_payment,monthly_salary)
print("The recomended portion to save: ", portion)


