import random

def main():
    num_dice = int(input("How many dice to roll? "))

    if num_dice <= 0:
        print("Please enter a positive number of dice.")
        return

    total_sum = 0
    for _ in range(num_dice):
        roll_result = random.randint(1, 6)
        print("Roll result for die", _ + 1, ":", roll_result)
        total_sum += roll_result

    print("Sum of the numbers:", total_sum)


if __name__ == "__main__":
    main()