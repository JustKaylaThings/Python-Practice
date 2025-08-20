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


def check_length(password):

    while len(password) <= 7:
        password = input("Too short. Enter a longer password: ")
        
    print("Success!")
    print(f"Length of password: {len(password)}")
    return password



#Variables
user_password = user_input()

#Call the result
good_password  = check_length(user_password)

#Print to file

with open("password.txt", "w") as file:
    file.write(f"Here's your password:\n{good_password}")

#Learned today: 
# while loop is for if you don't know when the end goal
# for loop is defnte end

#Still building on:
#writing to a file