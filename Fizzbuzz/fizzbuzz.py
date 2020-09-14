def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            if i == 42:
                print("Answer to the Ultimate Question of Life, the Universe, and Everything")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    main()