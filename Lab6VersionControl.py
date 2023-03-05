def encode_password(password):
    iter = 0  # counts iterations
    digit_list = [int(digit) for digit in password]
    while iter <= 7:
        digit_list[iter] += 3
        if digit_list[iter] > 9:
            digit_list[iter] -= 10
        iter += 1
    new_password = ''.join(str(digit) for digit in digit_list)
    return str(new_password)


while True:
    print('Menu', '-------------', '1. Encode', '2. Decode', '3. Quit', sep='\n')
    print()
    option = int(input('Please enter an option: '))
    if option == 1:
        pwd = str(input('Please enter your password to encode: '))
        encoded_pwd = encode_password(pwd)
        print('Your password has been encoded and stored!')
    elif option == 3:
        break


