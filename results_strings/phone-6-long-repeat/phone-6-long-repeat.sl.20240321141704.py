def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+106 769-858-438', Output: '769'
    # Input: '+83 973-757-831', Output: '973'
    # Input: '+62 647-787-775', Output: '647'
    
    # Find the index of the first space
    space_index = input_str.index(' ')
    
    # Get the substring starting from the index after the space
    numbers_after_space = input_str[space_index+1:]
    
    # Extract the first three numbers
    first_three_numbers = numbers_after_space[:3]
    
    return first_three_numbers

# Test the function with the provided inputs
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: '769'
print(get_first_three_numbers_after_space('+83 973-757-831'))   # Output: '973'
print(get_first_three_numbers_after_space('+62 647-787-775'))   # Output: '647'
