print("-------Welcome to temperature converter--------")
celsius = float(input("Enter Temperature in degree celcius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Fahrenheit: {fahrenheit}°F")

fahrenheit = float(input("Enter temperature in degree fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Celsius: {celsius}°C")

