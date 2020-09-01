def save_int():
    new_list = []

    while True:
        value = int(input("Skriv ett nummer för att spara det och '0' för att gå ur programmet: "))
        if value == 0:
            break
        else:
            new_list.append(value)

    sorted_list = sorted(new_list)
    print(sorted_list)


def main():
    save_int()


if __name__ == "__main__":
    main()
