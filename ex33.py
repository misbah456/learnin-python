def whileloops(i, numbers, x):

    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

    return

numbers = []

whileloops(0, numbers, 7)
