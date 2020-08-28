def reverse(input):
    new_str = ""
    i = -1
    while abs(i) <= len(input):
        new_str += input[i]
        i -= 1
    return new_str


def main():
    my_str = "Hej jag heter Andreas"
    print(reverse(my_str))


if __name__ == "__main__":
    main()
