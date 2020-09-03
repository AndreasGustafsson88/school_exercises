morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                   'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                   'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                   '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.'}


def morse_code(input):
    input_list = input.upper().split()
    answer_str = ""
    for i in range(len(input_list)):
        for letter in input_list[i]:
            if letter in morse_code_dict:
                answer_str += morse_code_dict[letter] + " "
    return answer_str


def morse_2code(text):
    answer_str = ""

    for letter in text:
        if letter.upper() in morse_code_dict:
            answer_str += morse_code_dict[letter.upper()] + " "
    return answer_str

def main():
    print(morse_code("Hello, world!"))
    print(morse_2code("Hello, world!"))


if __name__ == "__main__":
    main()