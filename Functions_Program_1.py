import random
def roll_dice():
    return random.randint(1, 6)

def main():
    roll_result = 0
    roll_count = 0

    while roll_result != 6:
        roll_result = roll_dice()
        roll_count += 1
        print("Roll", roll_count, "result:", roll_result)

    print("It took", roll_count, "rolls to get a 6.")

if __name__ == "__main__":
    main()
