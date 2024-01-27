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

user_input = input("Enter the cost of your dream home: ")
total_cost = float(user_input)
down_payment = total_cost * 0.25

def calc_months (a,b,c):
    down_payment = a
    monthly_salary = b
    portion_to_save = c

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


