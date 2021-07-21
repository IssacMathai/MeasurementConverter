
# List of measurements in inches
measurements = [5, 33.3, 5200]
converted = []

# Function retrieves a value, converts to inches and returns results
def to_cm(from_in):
    centimetres = (from_in * 2.54)
    return centimetres

# Retrieves values from 'measurements' list, converts to inches and places results in the 'converted' list
for item in measurements:
    result = to_cm(item)
    result_statement = "{} inches is {} centimetres.".format(item,result)
    converted.append(result_statement)
    
print(converted)