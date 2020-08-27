def max_of_three(num1, num2, num3):
    if num2 < num1 > num3:
        return num1
    elif num1 < num2 > num3:
        return num2
    else:
        return num3


def main():
    numbers = max_of_three(5, 9, 3)
    print(numbers)


if __name__ == "__main__":
    main()
