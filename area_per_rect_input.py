#!/usr/bin/env python3
# Created by: Santiago Hewett
# Date: Sep. 28,2023
# This program calculates the area and perimeter of a rectangle


import math


def main():
    print(
        "This program finds the area and perimeter of a rectangle that has your length and width calculations:"
    )
    print()
    # Declaring Variables
    length = float(input("Enter length of the rectangle (cm): "))
    width = float(input("Enter width of the rectangle (cm): "))
    print("The area is: {:.2f}cm^2".format(length * width))
    print("The perimeter is: {:.2f}cm".format(2 * (length + width)))


if __name__ == "__main__":
    main()
