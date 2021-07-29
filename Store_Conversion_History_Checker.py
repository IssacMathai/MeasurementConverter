# Empty list
measurements = []

# User inputs values
get_value = ""
while get_value !="done":
    get_value = input("Enter a value:")
    # When user inputs "done", stop asking for input
    if get_value == "done":
        break

    measurements.append(get_value)

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

else:
    print("Most recent values:")
    for value in measurements:
        print(measurements[len(measurements) - value - 1])