def main():
    even_number = ["2", "4", "6", "8"]
    for number in range(2221, 3001):
        number = str(number)
        num2 = list(number)

        if num2[0] in even_number and num2[1] in even_number and num2[2] in even_number and num2[3] in even_number:
            print(number, end=",")


if __name__ == "__main__":
    main()
