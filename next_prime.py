import prime_numbers


def next_prime(n):
    n = n + 1

    while True:
        if prime_numbers.prime(n):
            return n
        n += 1


def main():
    print(next_prime(25))
    n = input("Find the first prime larger than (Enter a number): ")
    n = int(n)
    print(next_prime(n))


if __name__ == "__main__":
    main()
