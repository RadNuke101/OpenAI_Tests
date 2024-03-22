def get_numbers_between_dash(input_str):
    # Prompt: return the three numbers in between "-" in input
    # Input: ['+106 769-858-438']
    # Output: 858
    input_str = input_str[0]  # Extract the input string from the list
    numbers = input_str.split('-')  # Split the input string by "-"
    output = numbers[1]  # Get the number between the dashes
    return output

# Test cases
print(get_numbers_between_dash(['+106 769-858-438']))  # Output: 858
print(get_numbers_between_dash(['+83 973-757-831']))  # Output: 757
print(get_numbers_between_dash(['+62 647-787-775']))  # Output: 787
