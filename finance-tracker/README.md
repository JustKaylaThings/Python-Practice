This script calculates the remaining balance of a user's income and expenses and displays the results into a separate file called "my_financial_report".

Topics Covered:

    - Functions
    - Return Variables
    - Unpacking or assigning multiple variables
    - Using a function within a function
    - If/else statements
    - Writing to a file

====

Hardest parts:

    - Unpacking

        def accessory():

            a = "bow"
            b = "tie"

            word = a + b

            return a, b, word

        a, b, word = accessory()

        print(f"This is my favorite {word}")

OUTPUT: This is my favorite bowtie

    - Calling a variable outside of the function to use it
