import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    num_sides = int(input("Enter the number of sides on the dice: "))
    roll_result = 0
    roll_count = 0

    while roll_result != num_sides:
        roll_result = roll_dice(num_sides)
        roll_count += 1
        print("Roll", roll_count, "result:", roll_result)

    print("It took", roll_count, "rolls to get a", num_sides)

if __name__ == "__main__":
    main()