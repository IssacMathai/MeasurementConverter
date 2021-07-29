# Empty list
measurements = []

# User inputs values
new_value = ""
while new_value !="done":
    new_value = input("Enter a value:")
    # When user inputs "done", stop asking for input
    if new_value == "done":
        break

    measurements.append(new_value)

# If list is empty, print message
if len(measurements) == 0:
    print("There are no measurements to display")

else:
    # Print whole list
    print("Whole List:")
    print(measurements)

    # Print most recent 4 values
    if len(measurements) >=4:
        print("Most recent 4 values:")
        for value in range(0,4):
            # Get length of list, print value and subtract 1 so that the next newest item will be printed in the next loop 
            print(measurements[len(measurements) - value - 1])

    # There are less than 4 values on the list so print what's on the list in order of most recent to least recent
    else:
        print("Most recent values:")
        for value in measurements:
            # Get length of list, print value and subtract 1 so that the next newest item will be printed in the next loop
            print(measurements[len(measurements) - measurements.index(value) - 1])