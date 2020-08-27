def main():
    n = int(input("Enter a number: "))
    new_dict = {}
    for i in range(1, n+1):
        new_dict[i] = i*i
    print(new_dict)


if __name__ == '__main__':
    main()
