#Task 1: Using the format function
def formatted_string(number):#here octal representation is used
    formatted_result = "{:o}".format(number)
    return formatted_result
result = formatted_string(145)
print("Formatted string is:", result)

#Task 2: Calculating the area of the pond and total water
import math
def calculate(radius):
    area=math.pi*radius**2
    water=1.4
    total_water=int(area*water)
    return area,total_water
radius=84
area,total_water = calculate(radius)
print("Area of the pond:", int(area))
print("Total amount of water in the pond:", total_water)

#Task 3: Calculating speed
def speed(distance,minutes):
    seconds=minutes*60
    s=distance/seconds
    return int(s)
distance=490
minutes=7
s=speed(distance, minutes)
print("Speed in meters per second:", s)