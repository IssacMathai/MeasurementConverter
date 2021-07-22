# List of measurements m metres
measurements = [5, 33.3, 5200]
converted = []

# Function retrieves a value, converts to feet and returns results
def to_ft(from_m):
    feet = (from_m * 3.281)
    return feet

# Retrieves values from 'measurements' list, converts to feet and places results m the 'converted' list
for item in measurements:
    result = to_ft(item)
    result_statement = "{} metres is {} feet.".format(item,result)
    converted.append(result_statement)
    
print(converted)

