from random import randint


def create_random_list(list_len, list_min, list_max):
    random_list = [randint(list_min, list_max) for number in range(0, list_len)]
    return random_list


def get_lowest_number(some_list):
    lowest_number = some_list[0]
    for number in some_list:
        if number < lowest_number:
            lowest_number = number
    return lowest_number


def get_highest_number(some_list):
    highest_number = some_list[0]
    for number in some_list:
        if number > highest_number:
            highest_number = number
    return highest_number

