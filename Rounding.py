# Input number
numbers = [5,33.3333,0.8888,0]
print(numbers)

#For each item in list, try converting to integer
for item in numbers:
    try:
        rounded_number = int(item)
        print(rounded_number)
# If number cannot be converted to integer, round to 2 dp
    except ValueError:
        print("{:.2f}".format(item))

