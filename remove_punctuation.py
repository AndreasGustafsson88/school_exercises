def remove_punctuation(input):
    #add " " so I don´t go out of range when counting i+1 if sentence is finished with {remove}
    input = f"{input} "
    new_str = ""
    remove = [":", ".", ",", "?", "!", "-", "_", "'", "´"]
    i = 0

    for letter in input:
        if letter in remove and not input[i+1].isalpha():
            i += 1
        else:
            new_str += letter
            i += 1

    return new_str.split()


def main():
    print(remove_punctuation("Hej: på??? nukö´r vi    di'g??"))


if __name__ == "__main__":
    main()
