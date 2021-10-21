#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This is the rounding number program in Python


def rounding_number(number_to_round, rounded_by_number):
    # this program rounds a number to a user inputted decimal place
    # process
    rounded_number = (number_to_round[0] * (10 ** rounded_by_number)) + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number / (10 ** rounded_by_number)

    number_to_round[0] = rounded_number


def main():
    # this function gets the # you are rounding and the # you're rounding by
    number_to_round_list = []

    # input
    number_to_round_string = input("Enter the number you want to round : ")
    rounded_by_number_string = input(
        "Enter how many decimal places you want to round by : "
    )

    try:
        # convert strings to respectly float and integer
        number_to_round = float(number_to_round_string)
        number_to_round_list.append(number_to_round)
        rounded_by_number = int(rounded_by_number_string)

        # call function
        rounding_number(number_to_round_list, rounded_by_number)

        # output
        # print the newly rounded float
        print("\nThe rounded number is {0}".format(number_to_round_list[0]))
    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
