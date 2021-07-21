
# List of measurements in centimetres
measurements = [5, 33.3, 5200]
converted = []

# Function retrieves a value, converts to inches and returns results
def to_in(from_cm):
    inches = (from_cm / 2.54)
    return inches

# Retrieves values from 'measurements' list, converts to inches and places results in the 'converted' list
for item in measurements:
    result = to_in(item)
    result_statement = "{} centimetres is {} inches.".format(item,result)
    converted.append(result_statement)
    
print(converted)


    
    