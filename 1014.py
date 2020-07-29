def main():

    x = input()
    y = input()

    x = int(x)
    y = float (y)

    consumo = x/y

    print("{:.3f} km/1".format(consumo))

if __name__ == "__main__":
    main()