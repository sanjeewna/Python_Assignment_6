def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters


def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons (negative to exit): "))

        if gallons < 0:
            print("Exiting program...")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters} liters.\n")


if __name__ == "__main__":
    main()