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

# Problem 4 (15 points):

country1 = "the-united-states-of-america"
country2 = "the People's Republic of China"
country3 = "jAPAN"
country4 = "Italian Republic"
country5 = "Great Socialist People's Libyan Arab Jamahiriya"

list1 = []
list1.append(country1.split('-')[1][0].upper())
list1.append('.')
list1.append(country1.split('-')[2][0].upper())
list1.append('.')
list1.append(country1.split('-')[4][0].upper())
list1.append('.')
list1 = "".join(list1)
print(list1)

list1 = []
list1.append(country2.split(' ')[1][0].upper())
list1.append(country2.split(' ')[2][0].upper())
list1.append(country2.split(' ')[4])
list1 = ".".join(list1)
print(list1)

list1 = []
list1.append(country3.split()[0][0].upper())
list1.append(country3.split()[0][1].lower())
list1.append(country3.split()[0][2].lower())
list1.append(country3.split()[0][3].lower())
list1.append(country3.split()[0][4].lower())
list1 = "".join(list1)
print(list1)

list1 = []
list1.append(country4.split()[0][0])
list1.append(country4.split()[0][1])
list1.append(country4.split()[0][2])
list1.append(country4.split()[0][3])
list1.append('y')
list1 = "".join(list1)
print(list1)

list1 = []
list1.append(country5.split(" ")[3][0])
list1.append(country5.split(" ")[3][1])
list1.append(country5.split(" ")[3][2])
list1.append(country5.split(" ")[3][3])
list1.append('a')
list1 = "".join(list1)
print(list1)
