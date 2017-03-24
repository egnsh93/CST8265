__author__ = 'shaneegan'


def main() :

    # Get the users cipher key
    key = get_input()

    # Get the users cipher message
    message = get_message()

    # Encrypt the message against the cipher
    encrypted_message = encrypt_message(key, message)

    # Decrypt the cipher to plain text
    decrypt_message(key, encrypted_message)


def get_input() :

    # Prompt for cipher key
    while True:

        key = input("\nEnter a shift key for Caesar Cipher (integer 0-25): ")

        # Check for an out of range key
        if key < 0 or key > 25:

            # Display error message and start the loop over
            print("\nKey out of range. Please try again.")
            continue

        else:

            break

    return key


def get_message() :

    # Prompt for cipher message
    while True:

        message = raw_input("\nEnter your message: ")

        # Check for an out of range key
        if not message:

            print("\nYou must enter a message. Please try again.")
            continue

        else:

            break

    return message


def encrypt_message(key, message) :

    encrypted_message = ""

    # Iterate through each character in the message
    for c in message:

        # Convert chars to ordinal value
        ordinal = ord(c)
        encrypted_ordinal = ordinal + key
        encrypted_char = chr(encrypted_ordinal)
        encrypted_message += encrypted_char

    print("\nThe cipher text of message '" + message + "' is : " + encrypted_message)

    return encrypted_message


def decrypt_message(key, message) :

    decrypted_message = ""

    # Iterate through each character in the message
    for c in message:

        # Convert chars to ordinal value
        ordinal = ord(c)
        decrypted_ordinal = ordinal - key
        decrypted_char = chr(decrypted_ordinal)
        decrypted_message += decrypted_char

    print("The recovered plain text is: " + decrypted_message + "\n")


main()
