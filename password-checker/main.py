#Password Strength Checker


"""

Needed:

criterion:
    characters(#$%^&)
    letters(kdsdnic)
    numbers(123456)

    Length(7+)

function that asks user to enter a Password
function that checks for the length of the Password len()

"""


def user_input():

    user_password = input("Enter a strong password: ")

    return user_password


def check_length(length):

    if len(length) <= 7:
        input("Too short. Enter a better password: ")
    else:
        print("Great password!")



#Variables
user_password = user_input()
password_length = len(user_password)

#Call the result
check_length(user_password)
print(f"Length of password: {password_length}")
