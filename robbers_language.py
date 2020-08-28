def translate(input_string):

    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    new_string = ""

    for letter in input_string:
        if letter.lower() in consonant:
            new_string += f"{letter}o{letter.lower()}"
        else:
            new_string += letter
    return new_string


def main():
    my_string = "Hej jag heter Andreas, kan du förstå mig?"
    print(translate(my_string))


if __name__ == "__main__":
    main()
