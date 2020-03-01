alpha_to_num = ''  
phone_number = '1'

while phone_number != 0:

    phone_number = input('Please enter a phone number in the xxx-xxx-xxx format: ')  

    for char in phone_number:

        if char >= 'A' and char <= 'C':
            alpha_to_num += '2'

        elif char >= 'a' and char <= 'c':
            alpha_to_num += '2'

        elif char >= 'D' and char <= 'F':
            alpha_to_num += '3'

        elif char >= 'd' and char <= 'f':
            alpha_to_num += '3'

        elif char >= 'G' and char <= 'I':
            alpha_to_num += '4'

        elif char >= 'g' and char <= 'i':
            alpha_to_num += '4'

        elif char >= 'J' and char <= 'L':
            alpha_to_num += '5'

        elif char >= 'j' and char <= 'l':
            alpha_to_num += '5'

        elif char >= 'M' and char <= 'O':
            alpha_to_num += '6'

        elif char >= 'm' and char <= 'o':
            alpha_to_num += '6'

        elif char >= 'P' and char <= 'S':
            alpha_to_num += '7'

        elif char >= 'p' and char <= 's':
            alpha_to_num += '7'

        elif char >= 'T' and char <= 'V':
            alpha_to_num += '8'

        elif char >= 't' and char <= 'v':
            alpha_to_num += '8'

        elif char >= 'W' and char <= 'Z':
            alpha_to_num += '9'

        elif char >= 'w' and char <= 'z':
            alpha_to_num += '9'

        else:
            alpha_to_num += char

    print("The phone number is:", alpha_to_num)
