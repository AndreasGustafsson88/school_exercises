def jh(string_input):
    vowels = ["a", "e", "i", "o", "u", "y"]
    new_output = ""

    for letter in string_input:
        if letter.lower() in vowels:
            new_output += letter.upper()
        else:
            new_output += letter

    print(new_output)


def main():
    jh("Hej jag heter Andreas")

if __name__ == "__main__":
    main()
