from my_methods import create_random_list, get_lowest_number, get_highest_number
from test import some_list

random_list = create_random_list(100, 0, 100)
print(f"Random list = {random_list}")

already_sorted_highest = 0
already_sorted_lowest = 0
highest_number_position = -1
lowest_number_position = 0
counter = 0

for item in random_list:
    highest_number = random_list[0]
    lowest_number = get_highest_number(random_list)

    if already_sorted_lowest + already_sorted_highest >= len(random_list):
        break

    for number in random_list[0 + already_sorted_lowest:len(random_list) - already_sorted_highest]:
        list_range = random_list[0 + already_sorted_lowest:len(random_list) - already_sorted_highest]
        counter += 1
        if number > highest_number:
            highest_number = number

        if number < lowest_number:
            lowest_number = number
#    print(random_list[0 + already_sorted_lowest:len(random_list) - already_sorted_highest])

    random_list[random_list.index(highest_number)], random_list[highest_number_position] \
        = random_list[highest_number_position], random_list[random_list.index(highest_number)]
#    print(f"First operation: {random_list}")

    random_list[random_list.index(lowest_number, lowest_number_position)], random_list[lowest_number_position] \
           = random_list[lowest_number_position], random_list[random_list.index(lowest_number, lowest_number_position)]
#    print(f"Second operation: {random_list}\n")

    highest_number_position -= 1
    lowest_number_position += 1
    already_sorted_highest += 1
    already_sorted_lowest += 1

print(f"Sorted list = {random_list}")
print(f"Counter = {counter}")
