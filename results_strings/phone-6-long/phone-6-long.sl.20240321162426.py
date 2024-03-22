def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+106 769-858-438', Output: '769'
    
    # Split the input string by space and get the second part
    second_part = input_str.split(' ')[1]
    
    # Extract the first three characters from the second part
    output = second_part[:3]
    
    return output

# Test cases
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: '769'
print(get_first_three_numbers_after_space('+83 973-757-831'))    # Output: '973'
print(get_first_three_numbers_after_space('+62 647-787-775'))    # Output: '647'
