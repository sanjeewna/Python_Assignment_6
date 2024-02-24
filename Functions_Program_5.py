def remove_odd_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list:", original_list)

    cut_down_list = remove_odd_numbers(original_list)
    print("Cut-down list (even numbers only):", cut_down_list)

if __name__ == "__main__":
    main()




