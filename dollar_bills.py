def main():
    names_stored = {
        1: "George Washington",
        2: "Thomas Jefferson",
        5: "Abraham Lincoln",
        10: "Alexander Hamilton",
        20: "Andrew Jackson",
        50: "Ulysses S.Grant",
        100: "Benjamin Frankling",
    }

    note = int(input("Vilken sedel är det du har?: "))

    if note in names_stored:
        print(names_stored[note])
    else:
        print("hörru du! den finns inte!")


if __name__ == "__main__":
    main()
