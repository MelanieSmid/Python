def convert_to_fahrenheit(celsius):
    """This function converts a celsius temp to a fahrenheit temp"""
    fahrenheit = 9.0/5.0 * celsius + 32
    return fahrenheit

for cel in range(0,101,10):
    print (cel, "\t", convert_to_fahrenheit(cel))
