def main():
    cities = []

    # Use a for loop to ask the user for city names and store them in the list
    for i in range(5):
        city_name = input("Enter the name of city {}: ".format(i + 1))
        cities.append(city_name)

    print("\nThe names of the five cities:")

    # Use a for loop to iterate through the list and print each city name
    for city in cities:
        print(city)


if __name__ == "__main__":
    main()