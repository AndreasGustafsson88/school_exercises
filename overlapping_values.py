def overlapping_values(input1, input2):

    for i in input1:
        if i in input2:
            return True
    return False


def overlapping_values1(input1, input2):

    for i in input1:
        for j in input2:
            if j == i:
                return True
    return False


def main():
    num1 = [1, 2, 3, 8]
    num2 = [5, 6, 7, 8]

    print(overlapping_values(num1, num2))
    print(overlapping_values1(num1, num2))


if __name__ == "__main__":
    main()
