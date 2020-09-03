from random import randrange

roll_result = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
               8: 0, 9: 0, 10: 0, 11: 0, 12: 0}


def roll_dice():
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)

    return dice1 + dice2


def main():
    for _ in range(1000):
        roll_result[roll_dice()] += 1
    print("Total".rjust(5), "|", "Simulated %".rjust(16), "|")
    print("----------------------------------")
    for i in roll_result:
        print(f"{i}".rjust(5), "|", f"{round(roll_result[i] / 1000 * 100, 2)}".rjust(16))


if __name__ == "__main__":
    main()
