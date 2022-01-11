#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 10, 2022
# This program allows a user to enter a positive number and then see
# all of the numbers up to that number squared


def main():

    # Print introduction message and get user input
    print("This program will display all of the positive numbers up" +
          " to a certain number squared.")
    print(" ")
    user_num = input("Enter a positive number: ")
    print(" ")

    try:
        # Make sure user input is an integer
        user_num_int = int(user_num)

        # Makes sure that user number is positive
        if user_num_int >= 0:
            # Loop that displays the squares of all of the numbers
            for counter in range(user_num_int + 1):
                power_of_two = counter ** 2
                print("{}^2 = {}".format(counter, power_of_two))

            # Print end message
            print(" ")
            print("Thanks for playing!")
        else:
            print("{} is not a positive number.".format(user_num_int))

    except Exception:
        # Prevent crash by displaying error message if user
        # input is not an integer
        print("'{}' is not a number".format(user_num))


if __name__ == "__main__":
    main()
