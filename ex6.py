# Set variable x to string with an embedded format string.
types_of_people = 10
# x = f"There are {types_of_people} types of people."

# set variable 'binary' to 'binary' = redundant slightly but needed
binary = "binary"
# set variable 'do_not' to 'don't'
do_not = "don't"
# set variable y to string with two embedded format strings
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

# Drill 

# Find all the places where a string is put inside a string. There are four places.


# x = "There are %d types of people." % 10
# binary = "binary"
# do_not = "don't"
# y = "Those who know %s and those who %s." %(binary, do_not)

# print x
# print y

# print "I said: %r." % x
# print "I also said: '%s'." % y

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation % hilarious

# w = "This is the left side of ..."
# e = "a string with a right side."

# print w + e