def divisible_multible(start, end):
    result = ""
    end = end + 1
    for number in range(start, end):
        if number % 7 == 0 and not number % 5 == 0:
            result += str(number) + ","
    return result


def main():
    print(divisible_multible(2000, 3200))


if __name__ == "__main__":
    main()
