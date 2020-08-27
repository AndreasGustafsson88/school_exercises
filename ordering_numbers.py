def main():
    X, Y, Z = 15, 10, 12
# X Smallest
    if Z > X < Y < Z:
        x, y, z = X, Y, Z
    elif Z > X < Y > Z:
        x, y, z = X, Z, Y
# Y Smallest
    elif X > Y < Z > X:
        x, y, z = Y, X, Z
    elif X > Y < Z < X:
        x, y, z = Y, Z, X
# Z Smallest
    elif X > Z < Y > X:
        x, y, z = Z, X, Y
    elif X > Z < Y < X:
        x, y, z = Z, Y, X

    print(x, y, z)


if __name__ == "__main__":
    main()
