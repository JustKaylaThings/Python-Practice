#Project #1: Finance Tracker


"""
Initial Requirements: 

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
    income = int(input("Enter your income for this month: $")) 
    expenses = int(input("Enter your expenses from the month: $"))

    balance = income - expenses
    return balance, income, expenses

balance, income, expenses = track_balance() #unpacking

#Calculate the percentage of expense to income ratio
def percentage_of(income,expenses):

    user_ratio = int(input("What is your preferred expense to ratio percentage?"))
    percentage = int((expenses/income) * 100)

    return percentage, user_ratio

percent, user_ratio = percentage_of(income,expenses) #unpacking

#If user's expenses is over 40% of their income, they get a warning
#Need an if statement
#Need the income and expenses
#Equation: If expenses 40% of income, then print warning


#Print the results
print("Your income: $", income)
print("Your expenses: $", expenses)
print("Your remaining balance: $", balance)
print("Expense to Income Ratio: ", percent, "%")

#WARNINGS
if percent <= 20:
    print("Great job! You have spent less than 40% of your monthly income.")
else:
    print("Warning: You have spent over 40% over your monthly income! RELAX!")


#Create a new file with the results
with open("my_financial_report", "w") as file:
    file.write(f"Your income: $ {income}\n")
    file.write(f"Your expenses: $ {expenses}\n\n")
    file.write(f"Your remaining balance: $ {balance}\n\n")
    file.write(f"Expense to Income Ratio: {percent}%\n")

    #WARNINGS
    if percent <= 20:
        file.write("Great job! You have spent less than 40% of your monthly income.")
    else:
        file.write("Warning: You have spent over 40% over your monthly income! RELAX!")


"""
First pass: calculate remaining balance (user input, functions)
2nd pass: calculate percentage (use a function within a function, unpacking, variable scope)
3rd pass: print warning if expense to ratio is larger than 40% (if/else conditions)
4th path: write the results to a file

"""

