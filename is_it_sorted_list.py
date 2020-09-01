def is_it_sorted(user_list):
    answer_list = sorted(user_list)
    if len(user_list) <= 1:
        return "Svårt att säga"
    else:
        if answer_list == user_list:
            return True
        elif user_list == sorted(user_list, reverse=True):
            return True
        else:
            return False


def main():
    new_list = []
    done = False

    while not done:
        value = int(input("Enter a number. 0 to exit: "))
        if value != 0:
            new_list.append(value)
        else:
            done = True

    print(is_it_sorted(new_list))


if __name__ == "__main__":
    main()
