def max_in_list(input1):
    largest = 0

    for i in input1:
        if i > largest:
            largest = i
    return largest


def main():
    my_list = [5, 7, 2, 6, 88, 99, 14]
    test = [5]
    print(max_in_list(my_list))
    print(max_in_list(test))


if __name__ == "__main__":
    main()
