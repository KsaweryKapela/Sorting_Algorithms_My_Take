from my_methods import create_random_list, get_lowest_number, get_highest_number

random_list = create_random_list(100, -100, 100)
print(f"Random list = {random_list}")

position = 0
iterated_number = get_lowest_number(random_list)

while iterated_number < get_highest_number(random_list):
    for number in random_list:
        if number == iterated_number:
            random_list[random_list[position:].index(number) + position], random_list[position] =\
                random_list[position], random_list[random_list[position:].index(number) + position]
            position += 1

    iterated_number += 1

print(f"Sorted list = {random_list}")

