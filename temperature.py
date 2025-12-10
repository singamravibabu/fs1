'''This file contains function to convert from one unit to another.
As of now it contains only one function.
However, we will add more functions in the future.'''

def to_fahrenheit(celsius):
    'This function converts celsius to fahrenheit.'
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def to_celsius(fahrenheit):
    'This function converts fahrenheit to celsius.'
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius