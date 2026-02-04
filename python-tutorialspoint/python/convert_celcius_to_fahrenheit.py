def celsius_to_fahrenheit(celsius):
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32  # Formula. F = (C x 9/5) + 32  
    return fahrenheit
# Calling the function
result = celsius_to_fahrenheit(37)
# Printing the result
print(result)