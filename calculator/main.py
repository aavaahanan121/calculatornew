import modules, sys

#VARIABLES

a_and_b = []

Input_raw = "nothing"

runing = True

cal = modules.calculator()

a = 0

b = 0

sign = ''

answer = ""

while runing:

    answer = ""

    a_and_b = "nothing"

    a = 0

    b = 0

    sign = ''


    Input_raw = input("\nplease enter your input seperated by space\n>")

    if Input_raw.upper() is "quit":

        sys.exit()

    a_and_b = Input_raw.split(" ")

    
#    print(a_and_b, Input_raw)
    try:
        a = int(a_and_b[0])

        b = int(a_and_b[2])
    except ValueError:

        print("Please enter a valid number\n")

        continue

    sign = a_and_b[1]

    if sign is '+':

        answer = cal.add(a, b)

    elif sign is '-':

        answer = cal.subtract(a, b)

    elif sign is '*':

        answer = cal.multiply(a, b)

    elif sign is '/':

        answer = cal.divide(a, b)

    else:
        print("Please input a valid input\n")

        continue
    
    print("\n Answer = ", answer)
    
