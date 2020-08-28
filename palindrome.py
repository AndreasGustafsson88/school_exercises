def palindrome(input):

    if input[::-1].lower() == input.lower():
        return True
    else:
        return False


def main():
    my_str = "Anna"
    print(palindrome(my_str))


if __name__ == "__main__":
    main()
