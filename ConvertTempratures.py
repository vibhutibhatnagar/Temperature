def convert_temperatures(temperature, unit):
    unit = unit.lower()  # Make input case-insensitive

    if unit == 'f':
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * 5 / 9
        return round(celsius, 2)

    elif unit == 'c':
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 9 / 5) + 32
        return round(fahrenheit, 2)

    else:
        return "Invalid unit. Use 'f' for Fahrenheit or 'c' for Celsius."
    
print(convert_temperatures(100, 'f'))  # Output: 37.78
print(convert_temperatures(0, 'c'))    # Output: 32.0
print(convert_temperatures(25, 'C'))   # Output: 77.0
