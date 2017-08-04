name = 'iSimoneChen'
age = 25 # not a lie
height = 3 # inches
weight = 100 # lbs not sure
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.") # "Let's talk about %s." % name
print(f"She's {height} inches tall.") # "She's %d inches tall." % height
print(f"She's {weight} pounds heavy.") # "She's %d pounds heavy." % weight
print("Actually that's not too heavy.") 
print(f"She's got {eyes} eyes and {hair} hair.") 
# "She's got %s eyes and %s hair." %(eyes, hair)
print(f"Her teeth are usually {teeth} depending on the coffee.") 
# "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.") 
# "If I add %d, %d, and %d I get %d." %(age, height, weight, a
# ge + height + weight)

# make a *string*, using `""` (double-quotes) around a piece of text
# embed variables inside a string, using a special `{}` sequence
# then put the variable you want inside the `{}` characters.
# start the string with the letter `f` for "format"

# Drill

# Try to write some variables that convert the inches and pounds to 
# centimeters and kilograms. Do not just type in the measurements.
# Work out the math in Python.

# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))

# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)

# print("Your height is : %d cm." % h_cm)