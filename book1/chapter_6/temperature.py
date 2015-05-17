def celsius_to_fahrenheit(temp_in_c):
    return float(temp_in_c) * 9 / 5 + 32

def fahrenheit_to_celsius(temp_in_f):
    return (float(temp_in_f) - 32) * 5 / 9


print "{} degrees C = {} degrees F".format(0, celsius_to_fahrenheit(0))
print "{} degrees C = {} degrees F".format(100, celsius_to_fahrenheit(100))
print "{} degrees C = {} degrees F".format(37, celsius_to_fahrenheit(37))

print "{} degrees F = {} degrees C".format(0, fahrenheit_to_celsius(0))
print "{} degrees F = {} degrees C".format(100, fahrenheit_to_celsius(100))
print "{} degrees F = {} degrees C".format(72, fahrenheit_to_celsius(72))
