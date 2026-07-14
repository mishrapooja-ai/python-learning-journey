def celsius_to_fahrenheit(celsius):
    return(celsius*9/5)+32
celsius=float(input("Enter a temperature in celsius:"))
fahrenheit=celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit=",fahrenheit)