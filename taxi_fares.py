base_fare = 4
price_140m = 0.25


def taxi_fares(distance):
    tot_price = ((distance//0.140)*price_140m) + base_fare
    return tot_price


def main():
    distance_travelled = 4
    print(taxi_fares(distance_travelled))


if __name__ == "__main__":
    main()
