def __prepare(message, alphabet):
    # Validate message and alphabet, set to upper and remove spaces
    alphabet = alphabet.replace(" ", "").upper()
    message = message.replace(" ", "").upper()

    # Check length and characters
    if len(alphabet) != 27:
        raise KeyError("Length of alphabet has to be 27.")
    for each in message:
        if each not in alphabet:
            raise ValueError("Each message character has to be included in alphabet!")

    # Generate dictionaries
    numbers = ("111", "112", "113", "121", "122", "123", "131", "132", "133", "211", "212", "213", "221", "222", "223", "231", "232", "233", "311", "312", "313", "321", "322", "323", "331", "332", "333")
    character2Number = {}
    number2Character = {}
    for letter, number in zip(alphabet, numbers):
        character2Number[letter] = number
        number2Character[number] = letter

    return message, alphabet, character2Number, number2Character

def encryptMessage(message, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period=5):
    message, alphabet, character2Number, number2Character = __prepare(message, alphabet)
    encrypted, encrypted_numeric = "", ""

    def __encryptPart(messagePart):
        one, two, three = "", "", ""
        tmp = []

        for character in messagePart:
            tmp.append(character2Number[character])

        for each in tmp:
            one += each[0]
            two += each[1]
            three += each[2]

        return one + two + three

    for i in range(0, len(message) + 1, period):
        encrypted_numeric += __encryptPart(message[i:i + period])

    for i in range(0, len(encrypted_numeric), 3):
        encrypted += number2Character[encrypted_numeric[i:i + 3]]

    return encrypted

def decryptMessage(message, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period=5):
    message, alphabet, character2Number, number2Character = __prepare(message, alphabet)
    decrypted_numeric = []
    decrypted = ""

    def __decryptPart(messagePart):
        tmp, thisPart = "", ""
        result = []

        for character in messagePart:
            thisPart += character2Number[character]

        for digit in thisPart:
            tmp += digit
            if len(tmp) == len(messagePart):
                result.append(tmp)
                tmp = ""

        return result[0], result[1], result[2]

    for i in range(0, len(message) + 1, period):
        a, b, c = __decryptPart(message[i:i + period])

        for j in range(0, len(a)):
            decrypted_numeric.append(a[j] + b[j] + c[j])

    for each in decrypted_numeric:
        decrypted += number2Character[each]

    return decrypted

if __name__ == '__main__':
    for i in range(10000):
        msg = "DEFEND THE EAST WALL OF THE CASTLE."
        encrypted = encryptMessage(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
        decrypted = decryptMessage(encrypted, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
        # print ("Encrypted: {}\nDecrypted: {}".format(encrypted, decrypted))
