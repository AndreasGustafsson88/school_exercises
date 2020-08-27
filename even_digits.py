def main():
    even_number = "2468"
    for number in range(1000, 3001):
        num1 = str(number)
        num2 = list(num1)

        if num2[0] in even_number and num2[1] in even_number and num2[2] in even_number and num2[3] in even_number:
            print(number, end=",")


if __name__ == "__main__":
    main()
