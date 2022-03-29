#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created March 2022
# This program prompts a user to enter a number
# and tells them what month it corresponds to.


def main():
    # this function gets a number and returns a month

    # input
    month_number = int(input("Enter the number of a month (ex: 3 for March): "))

    # process
    if month_number == 1:
        # output
        print("January")
    elif month_number == 2:
        print("February")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("Invalid Number - Make sure it is whole and between 1-12")

    print("\nDone.")


if __name__ == "__main__":
    main()
