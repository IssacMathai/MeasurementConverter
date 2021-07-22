# Input number
numbers = [5,33.3333,0.8888,0]
print(numbers)

for item in numbers:
    try:
        rounded_number = int(item)
        print(rounded_number)
    except ValueError:
        print("{:.2f}".format(item))

