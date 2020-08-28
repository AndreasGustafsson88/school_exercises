def filter_words(input1, input2):

    return [i for i in input1 if len(i) > input2]


def main():
    list_word = ["that", "take", "a", "list", "of", "words", "and", "returns", "the", "length", "longest"]
    print(filter_words(list_word, 3))

if __name__ == "__main__":
    main()
