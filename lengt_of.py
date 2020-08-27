def length_of(your_stuff):
    value = 0
    # Om input är en string
    for _ in your_stuff:
        value += 1
    return value


def main():
    print((length_of("hejaaa")))


if __name__ == "__main__":
    main()
