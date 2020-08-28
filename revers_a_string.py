def reverse(input):
    new_str = ""
    i = -1
    while abs(i) <= len(input):
        new_str += input[i]
        i -= 1
    return new_str


def reverse1(input):
    new_str = ""


    for i in range(len(input)-1, -1, -1):
        new_str += input[i]
    return new_str


def main():
    my_str = "Hej jag heter Andreas"
    print(reverse(my_str))
    print(reverse1(my_str))
    print(len(my_str))
if __name__ == "__main__":
    main()
