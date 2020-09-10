def prime_number(input_string):

    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    new_string = ""

    for letter in input_string:
        if letter.lower() in consonant:
            new_string += f"{letter}o{letter.lower()}"
        else:
            new_string += letter
    return new_string

def translate(inp):
    comparison = inp + "  "
    answer = ""
    i = 0
    while i < len(inp):
        if inp[i].lower() == comparison[i+2]:
            answer += inp[i]
            i += 3
        else:
            answer += inp[i]
            i += 1
    return answer

def main():
    my_string = "nu ska jag krama dig"
    print(prime_number(my_string))
    my_string2 = "Nonu soskoka Jojagog kokroramoma dodigog kokokoka"
    print(translate(my_string2))


if __name__ == "__main__":
    main()
