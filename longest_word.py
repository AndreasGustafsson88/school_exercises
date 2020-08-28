def longest_word(input1):
    longest = ""
    for i in input1:
        if len(i) > len(longest):
            longest = i
    return len(longest)


def main():
    my_words = ["that", "take", "a", "list", "of", "words", "and", "returns", "the", "length", "longest"]
    print(longest_word(my_words))

if __name__ == "__main__":
    main()
