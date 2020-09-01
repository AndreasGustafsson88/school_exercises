def unique_characters(str):
    return len(set(str))

# Andra lösningen med Dictionary
#    new_dict = {}
#    for letter in str:
#        new_dict[letter] = 1
#    return len(new_dict)


def main():
    print(unique_characters("hello, world!"))


if __name__ == "__main__":
    main()
