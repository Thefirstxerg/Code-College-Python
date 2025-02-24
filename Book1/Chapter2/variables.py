# Variable Creation
var1 = "very complicated string".title()

var2 = "value"

complete_variable = var1 + " " + var2
print(complete_variable)


# Formatting
var3 = 5    
formatted_var = f"{var1} {var2} {var3}"
print(formatted_var)


# Indentations and New Lines
varVeryBigString = "\n\nThis is a very big string that I want to split into two lines\n\tand I also want to have a tab space in the second line\n\n"
print(varVeryBigString)


# lStrip and rStrip and Strip
varStrip = "    This is a string with spaces at the beginning and at the end    "
print(varStrip.lstrip())
print(varStrip.rstrip())
print(varStrip.strip())


# Removing prefixes and suffixes
varPrefix = "https://www.google.com"
print(varPrefix.removeprefix("https://"))
print(varPrefix.removesuffix(".com"))


# Integers
varInt = 5
varInt2 = 5 + 5 * (10 / 2) * 3 - 1
print(varInt2)


# Multiple Assignments
x, y, z, w = 1, 2, 3, 4
print(x, y, z, w)



# Constants 
NEVER_CHANGE = 3.14159 
print(NEVER_CHANGE)


# Zen of Python
import this 