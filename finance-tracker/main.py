#Project #1: Finance Tracker


"""
Requirements: 

1. To track income and expenses
2. Subtract expenses from income
3. Allow user to input their own income and expanes for the month
4. Output remaining monthly balance


User inputs income
User inputs expenses

Script takes the two and subtracts them

"""

#Calculate the remaining monthly balance



def track_balance():
    #input auto converts to string. Numbers need int format
    income = int(input("Enter your income for this month:")) 
    expenses = int(input("Enter your expenses from the month: "))

    balance = income - expenses
    return balance, income, expenses

balance, income, expenses = track_balance()

#Calculate the percentage of expense to income ratio
def percentage_of(income,expenses):

    percentage = expenses/income
    user_friendly_percent = percentage * 100

    return percentage, user_friendly_percent

print("Your income: $", income)
print("Your expenses: $", expenses)
print("Your remaining balance: $" , balance)


#print(f"Your remaining balance for the month is: {track_balance()}")
#print(f"\nYou have spent {percentage_of(track_balance())} of your income.")


#If user's expenses is over 40% of their income, they get a warning
#Need an if statement
#Need the income and expenses
#Equation: If expenses 40% of income, then print warning

#expenses/
