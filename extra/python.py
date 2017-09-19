

# Problem 4 (15 points):

country1 = "the-united-states-of-america"
country2 = "the People's Republic of China"
country3 = "jAPAN"
country4 = "Italian Republic"
country5 = "Great Socialist People's Libyan Arab Jamahiriya"

list1 = []
list1.append(country1.split('-')[1][0].upper())
list1.append(country1.split('-')[2][0].upper())
list1.append(country1.split('-')[4][0].upper())
list1 = '.'.join(list1)
print(list1)

list1 = []
list1.append(country2.split(' ')[1][0].upper())
list1.append(country2.split(' ')[2][0].upper())
list1.append(country2.split(' ')[4])
list1 = '.'.join(list1)
print(list1)
