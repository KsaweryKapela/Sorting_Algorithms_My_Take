from my_methods import create_random_list

random_list = create_random_list(100, -100, 100)
print(f"Random list = {random_list}")

while True:
    checker = False
    for number in range(0, len(random_list) - 1):

        if random_list[number] > random_list[number+1]:
            random_list[number], random_list[number+1] = random_list[number+1], random_list[number]
            checker = True

    if not checker:
        break

print(f"Sorted list = {random_list}")
