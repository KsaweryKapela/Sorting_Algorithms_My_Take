from my_methods import create_random_list, get_lowest_number

random_list = create_random_list(100, -100, 100)
print(f"Random list = {random_list}")
already_sorted = -1
highest_number_position = 0

for item in random_list:
    highest_number = get_lowest_number(random_list)
    highest_number_position -= 1
    already_sorted += 1

    for number in random_list[0:len(random_list) - already_sorted]:
        if number > highest_number:
            highest_number = number
    random_list[random_list.index(highest_number)], random_list[highest_number_position] \
        = random_list[highest_number_position], random_list[random_list.index(highest_number)]

print(f"Sorted list = {random_list}")
