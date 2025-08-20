

"""

#Challenge #1
---------
Write a function called greet_user that:

Takes a name as a parameter
Returns a greeting message like "Hello, [name]!"
Call the function and print the result

"""

def greet_user(name):

    message = "Hello " + name

    return message


print(greet_user("Kayla"))

#ANOTHER WAY TO WRITE IT

def greet_user(name):

    return name

print(f"Hello {greet_user("Kayla")}")






"""

#Challenge #2
---------
Create a function called analyze_word that:

Takes a word as input
Returns three things: the word in uppercase, the word in lowercase, and the length of the word
Use unpacking to capture all three values
Print each result

"""


def analyze_word():

   word = input("Please enter a word: ")

   up = word.upper()
   low = word.lower()
   length = len(word)

   return word, up, low, length

word, up, low, length = analyze_word() #I'm not sure why I'm doing this. I just wrote it like this because that's how I remember doing  before. i don't underestand how i can just sett all of the values = to the function

print(up)
print(low)
print(length)


'''
Challenge #3

Write code that:

Asks the user for their favorite color and favorite animal
Writes both pieces of information to a file called "preferences.txt"
Each piece of info should be on a separate line

'''

def user_info():

    color = input("What is your favorite color?")
    animal = input("What is your favorite animal?")

    return color, animal

color, animal = user_info()

#write to prefernce.txt file

with open('preferences.txt', "w") as file:
    file.write(f"Favorite color: {color}\n")
    file.write(f"Favorite animal: {animal}\n")


"""

Challenge #4:
Create a mini program with two functions:

get_rectangle_info() - asks user for length and width, returns both
calculate_area(length, width) - calculates and returns the area
Use both functions together and save the results to a file

"""


def get_rectangle_info():

    user_length = int(input("Enter the length: "))
    user_width = int(input("Enter the width: "))

    return  user_length, user_width


def calculate_area(length, width): #These variables do not haev to be same as other variables. these are just place holders to be called. 

    area = length * width

    return area


user_length, user_width = get_rectangle_info()
area = calculate_area(user_length, user_width)

print(f"Area = {area}")


#Write results to file
with open("result.txt", "w") as file:
    file.write(f"Area: {area}")

#Duration: 40 mins