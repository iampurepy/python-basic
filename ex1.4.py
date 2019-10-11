#REMMEMBER
"""
a variable is a name for something, similar to YOUR name,
“Zed,” is a name for “the human who wrote this book.” 
variable names must to make code read more like English and because they have lousy memories. If they didn’t use good names
for things in their software, they’d get lost when they tried to read their code again.
"""
#Difference between = (single-equal) and == (double-equal)
#Should x = 100 not x=100,
#You should add space around operators like this so that it’s easier to read.


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")
