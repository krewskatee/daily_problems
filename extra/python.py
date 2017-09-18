def area_triangle(base, height):
    area = (base*height)/2
    return area

def area_circle(pi, radius):
    area = round((pi*(radius*radius)), 2)
    return area

def memory_in_bits(target):
    length = 0
    while (target):
        target >>= 1
        length += 1
    return(length)

def memory_in_bytes(target):
    length = 0
    while (target):
        target >>= 1
        length += 1
    return(int(length/8))


# Problem 1 (5 points):
# Compute the area of a triangle.
# Formula: (base*height)/2
# Complete line 9 and 10

base = height = 5

output_string = "The area of the triangle is %s." % (area_triangle(5, 5))
print (output_string)

# """
# Problem 2 (5 points):
# Compute the area of a circle.
# Formula: PI*radius*radius
# Complete line 24 and 25
# """
import math
PI = math.pi
radius = 10

output_string = "The area of a circle with a radius of %s is %s." % (radius, area_circle(PI, radius))
print (output_string)

"""
Problem 3 (5 points):
Check the memory usage for the target integer.
Complete line 35 to 37
"""
target = 12345678

print("Integer: %s" % (target))
print("Memory: %s bits or %s bytes." % (memory_in_bits(target), memory_in_bytes(target)))
