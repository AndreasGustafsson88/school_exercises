def main():
    print("Plz write how many steps you would like your robot to take")
    up = int(input("Up: "))
    down = int(input("Down: "))
    left = int(input("Left: "))
    right = int(input("Right: "))

    vertical = up - down
    lateral = left - right

    distance = (vertical**2 + lateral**2)**0.5

    if distance == 0:
        print("Lol, look at that! Seems like you didn't get anywhere at the end")
    else:
        print(f"You are now {int(distance)} steps away from where you started")


if __name__ == "__main__":
    main()
