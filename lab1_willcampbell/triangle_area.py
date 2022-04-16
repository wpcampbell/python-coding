# This program calculates the area of a triangle.

# This block first prints out the term "This program finds the area of a triangle." and then prints a blank line
print("This program finds the area of a triangle.")
print()

# This block asks for a number from the user with a decimal point (float) from the user in order to find the area of the given triangle
height = float(input("Please enter the height of the triangle: "))
base = float(input("Please enter the base length of the triangle: "))

# This block creates the variable 'area' and defines it as 0.5 times the given height and base in the previous block
area = 0.5 * height * base

# This block summarizes the given height and base while also giving the solution to the variable 'area' based on the information given by the user. E.g. if height =2.0
# and base = 4.0 then 0.5*2.0*4.0 would give the output "The area of a triangle with height 2.0 and base 4.0 is 4.0"
print("The area of a triangle with height", height, "and base", base, "is", area, ".")
