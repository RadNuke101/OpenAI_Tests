def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+106 769-858-438'
    # Output: '769'
    
    # Split the input string by space
    parts = input_str.split()
    
    # Get the second part (numbers after the space)
    numbers_after_space = parts[1]
    
    # Extract the first three numbers
    first_three_numbers = numbers_after_space[:3]
    
    return first_three_numbers

# Test the function with the provided inputs
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: '769'
print(get_first_three_numbers_after_space('+83 973-757-831'))   # Output: '973'
print(get_first_three_numbers_after_space('+62 647-787-775'))   # Output: '647'
print(get_first_three_numbers_after_space('+172 027-507-632'))  # Output: '027'
print(get_first_three_numbers_after_space('+72 001-050-856'))   # Output: '001'
print(get_first_three_numbers_after_space('+95 310-537-401'))   # Output: '310'
769
973
647
027
001
310
