# Input number
number = input("Enter a number")
print(number)

# Convert to float
try:
    new_number = float(number)
    print(new_number)
# Round up to two decimal places
except ValueError:
    print("{:.2f}".format(new_number))

