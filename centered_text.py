def centered_text(input1, input2):
    spaces = input2 * " "
    new_string = f"{spaces}{input1}{spaces}"
    return new_string


def main():
    print(centered_text("hej", 10))


if __name__ == "__main__":
    main()
