def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Given input as ['+106 769-858-438'] output is 769
    # Given input as ['+83 973-757-831'] output is 973
    # Given input as ['+62 647-787-775'] output is 647
    space_index = input_str.index(' ')
    numbers = input_str[space_index+1:space_index+4]
    return numbers

# Test cases
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: 769
print(get_first_three_numbers_after_space('+83 973-757-831'))  # Output: 973
print(get_first_three_numbers_after_space('+62 647-787-775'))  # Output: 647
