#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on December 2019
# This program finds the largest number in the list of numbers given

import random


def smallest_num(list_of_numbers):
    #

    smallest = list_of_numbers[0]

    for single_number_in_list in list_of_numbers:
        if single_number_in_list < smallest:
            smallest = single_number_in_list

    return smallest


def main():
    #

    random_numbers = []
    lowest_num = 0

    # input
    print("The numbers are: ")
    for loop_counter in range(0, 10):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    lowest_num = smallest_num(random_numbers)

    print("The smallest number is: {0} ".format(lowest_num))


if __name__ == "__main__":
    main()
