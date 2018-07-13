
def scores():
    list_of_scores = []

    user_input = str(input("Enter your first score."))  # starting the program
    # if we want user to be able to type in a word, we must input value as a string
    print("You entered", user_input)  # confirming their input

    while user_input != str("quit"):  # loop will allow user to input many values
        user_input = float(user_input)  # converting string to float
        #  The if/else statement is extra to force the user to not use a negative number.
        if user_input >= 0:
            list_of_scores.append(user_input)  # if the value user entered is positive, add it to list
            user_input = str(input("Enter your next score. Type quit to calculate your average."))
            print("You entered", user_input)   # confirming their input
        else:  # if value user entered is not positive, tell them to input a positive number
            print("Incorrect value entered. Please enter a percentage.")
            user_input = str(input("Enter your next score. Type quit to calculate your average."))

    # the loop is over

    test_average = sum(list_of_scores)/len(list_of_scores)  # sum adds the scores, len counts how many items in list
    print("You received a", test_average, "percent in the class.")  # output information to user

    if test_average >= 90:
        print("You have received an A in the class.")

    elif 80 <= test_average < 90:
        print("You have a received a B in the class.")

    elif 70 <= test_average < 80:
        print("You have received a C in the class.")

    elif 60 <= test_average < 70:
        print("You have received a D in the class.")

    else:
        print("You have received an F in the class.")


print("Welcome to the grade average calculator.")
scores()
print("End Program")
