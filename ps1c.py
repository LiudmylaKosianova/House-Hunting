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
r = 0.04 #annual return from the current_savings investments
semi_anual_raise = 0.7 #pay raise the user gets every half of the year



user_input = input("Enter your annual salary: ")
annual_salary = float(user_input)

user_input = input("Enter the cost of your dream home: ")
total_cost = float(user_input)

 


monthly_salary = annual_salary / 12 #calculate the monthly salary of the user
#base = portion_saved * monthly_salary #calculate the base amount to be saved every month
current_savings = 0.0

count = 0

while down_payment > current_savings:
    current_savings += (current_savings * (r/12)) + base
    count += 1
    if count%6 == 0:
        monthly_salary += monthly_salary*semi_anual_raise
        base = portion_saved * monthly_salary

    
print("Number of months: ", count)

