def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2: Decode")
    print("3: Exit")
def encode(password):

    x = 0
    encoded_password = ""
    for char in password:
        char_value = int(char)

        if char_value < 7:
            encoded_password += str(char_value + 3)
        else:
            value = str(char_value + 3)
            char_value = value[1]
            encoded_password += char_value

    return encoded_password

if __name__ == '__main__':
    while True:
        menu()
        user_input = input("\nPlease enter an option: ")
        if user_input == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            print("The encoded password is " + encoded_password + " , and the original password is " + password + ".")
        elif user_input == "3":
            break
