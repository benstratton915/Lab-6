def encode_password(password):  # encodes a new password where each digit is changed by +3
    iter = 0  # counts iterations
    digit_list = [int(digit) for digit in password]  # converts string to list of ints
    while iter <= 7:
        digit_list[iter] += 3
        if digit_list[iter] > 9:
            digit_list[iter] -= 10
        iter += 1
    new_password = ''.join(str(digit) for digit in digit_list)  # reconverts list back to string
    return str(new_password)


def decode_password(encoded_pwd_arg):
    decoded_pwd = ""
    for i in encoded_pwd_arg:
        raw_pwd = int(i) - 3
        if raw_pwd < 0:
            raw_pwd += 10
        decoded_pwd += str(raw_pwd)
    return decoded_pwd


while True:
    print('Menu', '-------------', '1. Encode', '2. Decode', '3. Quit', sep='\n')
    print()
    option = int(input('Please enter an option: '))
    if option == 1:
        pwd = str(input('Please enter your password to encode: '))
        encoded_pwd = encode_password(pwd)
        print('Your password has been encoded and stored!\n')
        # print(encoded_pwd)
    elif option == 2:
        print(f"The encoded password is {encoded_pwd}, and the original password is {decode_password(encoded_pwd)}.\n")
    elif option == 3:
        break


