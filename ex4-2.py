numbers = [1, 3, 6, 123, 345, 5745,56]

with open( "./data/outex4-2-1.txt", "w" ) as output:
    for number in numbers:
        output.write(str(number) + '\n')

