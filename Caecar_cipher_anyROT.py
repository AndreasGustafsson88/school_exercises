key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
       'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']


def encipher(code):
    new_str = ""
    rot = 9
    for letter in code:
        if letter in key:
            if key.index(letter) < 26 - rot:
                new_str += key[key.index(letter) + rot]
            elif 26 <= key.index(letter) <= 51 - rot:
                new_str += key[key.index(letter) + rot]
            else:
                new_str += key[key.index(letter) - 26 + rot]
        else:
            new_str += letter

    return new_str


def decipher(code):
    new_str = ""
    rot = 9
    for letter in code:
        if letter in key:
            if key.index(letter) < 0 + rot:
                new_str += key[key.index(letter) + 26 - rot]
            elif 26 <= key.index(letter) < 26 + rot:
                new_str += key[key.index(letter) + 26 - rot]
            else:
                new_str += key[key.index(letter) - rot]
        else:
            new_str += letter

    return new_str


def main():
    print(encipher("Hello, my name is Andreas and I like discgolf!"))
    print(decipher("Qnuux, vh wjvn rb Jwmanjb jwm R urtn mrblpxuo!"))


if __name__ == "__main__":
    main()
