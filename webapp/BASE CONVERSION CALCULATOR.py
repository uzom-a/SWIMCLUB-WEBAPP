#BASE CONVERSION CALCULATOR

convert = int(input('''Enter
 1 for Decimal to Binary
 2 for Binary to Decimal
 3 for Decimal to Hexadecimal
 4 for Hexadecimal to Decimal
 5 for Binary to Hexadecimal
 6 for Hexadecimal to Binary: '''))


# Convert Decimal to Binary
def DecimalToBinary(number):
    if number == None:
        number = int(input("Enter a decimal number: "))
    remainder = []
    while number != 0:
        remainder.append(number % 2)
        number = number // 2
        result = remainder[::-1]
        for num in result:
            answer = print(num, end="")
    return answer
    


# Convert Binary to Decimal
def BinaryToDecimal():
    binary = list(input("Enter the binary number: "))
    
    power = 0
    output = 0
    while binary:
        last_digit = binary.pop()
        output = int(last_digit) * (2 ** power) + output
        power += 1
    return output


#Convert Decimal to Hexadecimal
def DecimalToHexadecimal():
    number = int(input("Enter the decimanl number: "))
    if number == 0:
        return "0"

    hexadecimal = ""

    while number > 0:
        remainder = int(number) % 16 
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        elif remainder == 10:
            hexadecimal = "A" + hexadecimal
        elif remainder == 11:
            hexadecimal = "B" + hexadecimal
        elif remainder == 12:
            hexadecimal = "C" + hexadecimal
        elif remainder == 13:
            hexadecimal = "D" + hexadecimal 
        elif remainder == 14:
            hexadecimal = "E" + hexadecimal
        elif remainder == 15:
            hexadecimal = "F" + hexadecimal       
        number = int(number) // 16
    return hexadecimal



#Convert Hexadecimal to Decimal
def HexadecimalToDecimal(number):
    if number == None:
        number = list(input("Enter the Hexadecimal(must be uppercase): "))  #made the user input into a list so that we can pop it
    power = 0
    output = 0
    while number:
        last_digit = number.pop()
        if last_digit == "A":
            last_digit = 10
        elif last_digit == "B":
            last_digit = 11
        elif last_digit == "C":
            last_digit = 12
        elif last_digit == "D":
            last_digit = 13
        elif last_digit == "E":
            last_digit = 14
        elif last_digit == "F":
            last_digit = 15   
        output = int(last_digit) * (16 ** power) + output
        power += 1
    return output
    


# Convert Binary to Hexadecimal

def BinaryToHexadeximal():
    binary = input("Enter the binary number: ")
    
    # Check if the length of string is divisible by 4, if not, add zeros to the make it divisible by 4
    while len(binary) % 4 != 0:
        binary = "0" + binary
    
        hexadecimal = ""

    for x in range(0, len(binary), 4):
        group = binary[x: x + 4]

        power = 3
        output = 0

    for digit in group:
        output += int(digit) * (2 ** power)
        power -= 1
                
    if output < 10:
        hexadecimal += str(output)
    elif output == 10:
        hexadecimal += "A"
    elif output == 11:
        hexadecimal += "B"
    elif output == 12:
        hexadecimal += "C"
    elif output == 13:
        hexadecimal += "D"
    elif output == 14:
        hexadecimal += "E"
    elif output == 15:
        hexadecimal += "F"
    return hexadecimal



def HexadecimalToBinary():
    hexadecimal = list(input("Enter the hexadecimal(must be uppercase):"))
    decimal = HexadecimalToDecimal(hexadecimal)
    return DecimalToBinary(decimal)


if convert == 1:
    print(DecimalToBinary())
elif convert == 2:
    print(BinaryToDecimal())
elif convert == 3:
    print(DecimalToHexadecimal())
elif convert == 4:
    print(HexadecimalToDecimal())
elif convert == 5:
    print(BinaryToHexadeximal())    
elif convert == 6:
     HexadecimalToBinary()
else:
    print("Invalid output")

