# List of test case values
numbers = [5,33.3333,0.8888,0]
print(numbers)

# For each item in list
for item in numbers:
    # If there is no remainder, print to 0dp
    if item%1 == 0:
        print("{:.0f}".format(item))
    # Else, print to 2dp
    else:
        print("{:.2f}".format(item))


