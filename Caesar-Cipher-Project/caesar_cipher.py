alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt():
    message = input("Enter message: ")

    try:
        key = int(input("Enter key (0-25): "))

        if key < 0 or key > 25:
            print("Key must be between 0 and 25.")
            return

    except ValueError:
        print("Invalid key. Please enter a number.")
        return

    result = ""

    for letter in message.upper():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + key) % 26
            result = result + alphabet[new_position]
        else:
            result = result + letter

    print("Encrypted message:", result)


def decrypt():
    message = input("Enter message: ")

    try:
        key = int(input("Enter key (0-25): "))

        if key < 0 or key > 25:
            print("Key must be between 0 and 25.")
            return

    except ValueError:
        print("Invalid key. Please enter a number.")
        return

    result = ""

    for letter in message.upper():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - key) % 26
            result = result + alphabet[new_position]
        else:
            result = result + letter

    print("Decrypted message:", result)


choice = ""

while choice != "3":
    print("\nCAESAR CIPHER")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        encrypt()

    elif choice == "2":
        decrypt()

    elif choice == "3":
        print("Program ended.")

    else:
        print("Invalid choice. Select 1, 2 or 3.")
