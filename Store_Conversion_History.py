# Empty list
measurements = []

# User inputs 6 values
for value in range(0,6):
    get_value = input("Enter a value.")
    measurements.append(get_value)

# Print whole list
print("Whole List:")
print(measurements)

# Print most recent 4 values
print("Most recent 4 values:")
for value in range(0,4):
    print(measurements[len(measurements) - value - 1])