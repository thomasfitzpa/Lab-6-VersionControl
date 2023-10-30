def encode(password):

    x = 0
    encoded_password = ""
    for char in password:
        char_value = int(char)

        if char_value < 6:
            encoded_password += str(char_value + 4)
        else:
            value = str(char_value + 4)
            char_value = value[1]
            encoded_password += char_value

    return encoded_password


print(encode("123456789"))
