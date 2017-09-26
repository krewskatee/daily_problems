def decimal_to_binary(decimal_number):
    x=decimal_number
    binary_array=[]
    while (decimal_number>0):
        a=int(float(decimal_number%2))
        binary_array.append(a)
        decimal_number=(decimal_number-a)/2
    binary_array.append(0)
    string=""
    for j in binary_array[::-1]:
        string=string+str(j)
    print('The binary no. for %d is %s'%(x, string))

def binary_to_decimal(binary_number):

    binary_list = list(binary_number)
    binary_length = len(binary_list)

    index = 0
    power = binary_length - 1
    total = 0

    while(power >= 0):
        total += (int(binary_list[index])) * (2**(power))
        index += 1
        power -= 1
    print(total)



decimal_number = int(input("Please enter a decimal number: "))
decimal_to_binary(decimal_number)
binary_number = input("Please enter binary number: ")
binary_to_decimal(binary_number)
