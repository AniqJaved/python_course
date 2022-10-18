"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
1. Implement pi*r^2 in the code.

"""

pi = 3.142
radius = input('Enter radius of Circle : ')
area = pi*((int(radius)**2))
print(f"Radius of circle is : {area}")