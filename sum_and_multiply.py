def sum(input):
    value = 0

    for i in input:
        value += i
    return value


def multiply(input):
    value = 1

    for i in input:
        value *= i
    return value


def main():
    numbers = [1, 2, 3, 4]
    print((sum(numbers)))
    print(multiply(numbers))


if __name__ == "__main__":
    main()
