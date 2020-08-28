def prime(input):
    if input <= 1:
        return False
    for x in range(2, input):
        if input % x == 0:
            return False
    return True


def main():
    for x in range(100):
        print(x)


if __name__ == "__main__":
    main()
