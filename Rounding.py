number = input("Enter a number")
print(number)

try:
    new_number = float(number)
    print(new_number)
except ValueError:
    print("{:.2f}".format(new_number))

