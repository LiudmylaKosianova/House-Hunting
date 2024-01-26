"""
A program calculates how many months it will take a user to save up enough money 
for a down payment for a dream house. 
The programm assumes the user has some investments that return 4% annually. 

"""

annual_salary = 0.0
monthly_salary = annual_salary / 12 
portion_saved = 0.0 #a portion of salary to be saved every month
total_cost = 0.0 #cost of a house
portion_down_payment = 0.25 #the portion of a cost needed for the down payment is 25%
r = 0.04 #annual return from the current_savings investments

user_input = input("Enter your annual salary: ")
annual_salary = float(user_input)

user_input = input("Enter the percent of your salary to save: ")
portion_saved = float(user_input) / 100

user_input = input("Enter the cost of your dream home: ")
total_cost = float(user_input)


