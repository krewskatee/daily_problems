def area_triangle(base, height):
    return (base*height)/2

def area_circle(radius):
    import math
    PI = math.pi
    return (PI*radius**2)

# """
# Problem 2 (5 points):
# Compute the area of a circle.
# Formula: PI*radius*radius
# Complete line 24 and 25
# """

radius = 10

output_string= "Area of cirlce is %s." % (round(area_circle(10), 2))
print (output_string)
