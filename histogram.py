def hist1(input1):

    for i in input1:
        for _ in range(i):
            print("*", end="")
        print("")


def main():
    my_list = [2, 5, 3]
    print((histogram(my_list)))
    hist1(my_list)


if __name__ == "__main__":
    main()
