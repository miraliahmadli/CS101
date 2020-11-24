import math

#--------------------------------------------------------------#
#
# Function dec_to_any
#
# Input:
#		n: number to convert
#		radix: radix to use
#
# Output:
#		new_num: converted number
#
#--------------------------------------------------------------#
def dec_to_any_list(n,radix):
    converted_number = []
    while n != 0:
        converted_number.append(str(n % radix))
        n //= radix
    converted_number.reverse()
    return "".join(converted_number)


def dec_to_any_string(n, radix):
    converted_number = ""
    while n != 0:
        converted_number += str(n % radix)
        n //= radix
    new_num = converted_number[::-1]
    return new_num


#--------------------------------------------------------------#
#
# Function main
#
# This is the driver function
# Do commandline input/output and formatting here
#
#		Example:
#		Enter a number: 61
#		Enter a radix: 16
#		61 in base 10 is 3D in base 16
#
#
# Just digits, no gap or another character
# 123 (O)    ‘1’ ‘2’ ‘3’ (x)
# “Wrong input!!!” if inputs are not in range
# You must use the formatting operator % (TAs will check!!!)

#--------------------------------------------------------------#

def main():
    num = input("Enter a number: ")
    try:
        num = int(num)
        if num <= 0:
            print("Wrong input")
            return
    except:
        print("Wrong input")
        return
    radix = input("Enter a radix: ")
    try:
        radix = int(radix)
        if not(2 <= radix <= 16):
            print("Wrong input")
            return
    except:
        print("Wrong input")
        return
    new_num = dec_to_any_string(num, radix)
    print("%d in base 10 is %s in base %d" % (num, new_num, radix))


main()
