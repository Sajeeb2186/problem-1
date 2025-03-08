def find_largest_number(numbers):
    """
    This function takes a list of numbers and returns the largest number within it. 
    """
    largest = numbers[0]  # Initialize largest with the first element
    for num in numbers:
        if num > largest:
            largest = num
    return largest 

# Example usage
number_list = [10, 5, 20, 3, 8]
result = find_largest_number(number_list)
print("The largest number is:", result) 