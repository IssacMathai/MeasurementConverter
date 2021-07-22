# List of measurements in feet
measurements = [5, 33.3, 5200]
converted = []

# Function retrieves a value, converts to metres and returns results
def to_m(from_ft):
    metres = (from_ft / 3.281)
    return metres

# Retrieves values from 'measurements' list, converts to metres and places results m the 'converted' list
for item in measurements:
    result = to_m(item)
    result_statement = "{} feet is {} metres.".format(item,result)
    converted.append(result_statement)
    
print(converted)

