def generate_characters(input1, input2):
    new_word = ""

    for i in range(input1):
        new_word += input2
    return new_word


def gene_test(input1, input2):
    return input1 * input2


def main():
    num = 5
    character = "h"
    print(generate_characters(num, character))
    print(gene_test(num, character))


if __name__ == "__main__":
    main()
