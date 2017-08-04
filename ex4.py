# using = to make names for things like cars, drivers and passengers.
# Number of total cars
cars = 100
# Number of spaces in each car
space_in_a_car = 4.0
# Number of total drivers
drivers = 30
# Number of total passengers
passengers = 90
# Number of cars_not_driven
cars_not_driven = cars - drivers
# Each driver represents a car driven
cars_driven = drivers
# All the cars times the space in each car equals the total capacity
carpool_capacity = cars_driven * space_in_a_car
# The average number of passengers is all passengers divided by total cars driven
average_passengers_per_car = passengers / cars_driven


# telling OS X what to display, numbers instead of names or variables
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.") 
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# _, underscore character, to put an imaginary space between words in **variable names

# drill

# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# The NameError above is due to the fact that the author typed 
# `car_pool_capacity` but the actual variable is `carpool_capacity`, no
# underscore character between 'car' and 'pool'.
# NameError means the 'name' of the variable is unknown or has not yet 
# been defined.

# Why do we use 4.0 instead of 4?
# What happens if it's just 4?

# 4.0 is a floating point number, while 4 is an integer.
# floating point numbers can represent fractions, while integers cannot.
# If the integer `4` was used vs. `4.0`, the `carpool_capacity` would be
# integer `120` vs. floating point `120.0`. The floating point is not 
# necessary here in this case, but it doesn't hurt and is good practice to
# consider.

# what does `^^` mean in phlipper's answer, make any sense or just a special
# mark of himself?

# [lpthw/ex4.py at master · phlipper/lpthw](https://github.com/phlipper/lpthw/blob/master/ex4.py)
# [My Python Learning Journal: LPTHW - Exercise 4](https://python-learning-journal.blogspot.jp/2011/08/lpthw-exercise-4.html?showComment=1501807929200#c6300688133111531961)