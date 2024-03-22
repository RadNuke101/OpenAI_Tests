def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+106 769-858-438', Output: '769'
    
    # Find the index of the first space
    space_index = input_str.index(' ')
    
    # Extract the numbers after the space
    numbers_after_space = input_str[space_index+1:space_index+4]
    
    return numbers_after_space

# Test cases
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: '769'
print(get_first_three_numbers_after_space('+83 973-757-831'))    # Output: '973'
print(get_first_three_numbers_after_space('+62 647-787-775'))    # Output: '647'
