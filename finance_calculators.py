# This is a program that allow users to calculate their investment or their home loan repayments.
import math

# Menu
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond \t - to calculate the amount you'll have to pay on a home loan")
print()
user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Investment calculator.
if user_selection.lower() == "investment":
    investment_amount = float(input("Please enter the amount you'd like to deposit: "))
    investment_interest = float(input("Please enter the interest rate: "))
    investment_years = int(input("Please enter the number of years you'd like to invest for: "))
    investment_interest_type = input("Please select either 'simple' or 'compound' interest type: ")
    # Simple interest calculator.
    if investment_interest_type.lower() == "simple":
        simple_total = investment_amount * ( 1 + investment_interest / 100 * investment_years)
        print(f"£{investment_amount} invested at {investment_interest}% interest rate for {investment_years} years with {investment_interest_type.lower()} interest will result in £{round(simple_total, 2)} at the end.")
    # Compound interest calculator.
    elif investment_interest_type.lower() == "compound":
        compound_total = investment_amount * math.pow((1 + investment_interest / 100), investment_years)
        print(f"£{investment_amount} invested at {investment_interest}% interest rate for {investment_years} years with {investment_interest_type.lower()} interest will result in £{round(compound_total, 2)} at the end.")
    # If user typed anything else.
    else:
        print("Invalid entry")

# Bond calculator.
elif user_selection.lower() == "bond":
    bond_amount = float(input("Please enter the current full value of the property: "))
    bond_interest = float(input("Please enter the interest rate: "))
    bond_months = int(input("Please enter the number of months you'd like to take to repay this: "))
    bond_monthly_repayment = ( bond_interest / 100 / 12 * bond_amount ) / ( 1 - ( 1 + bond_interest / 100 / 12 ) ** ( - bond_months ))
    print(f"To pay off £{bond_amount} with {bond_interest}% interest rate in {bond_months} months, your monthly payment will be £{round(bond_monthly_repayment, 2)}.")

# If user inputs anything else.
else:
    print("Invalid entry")
