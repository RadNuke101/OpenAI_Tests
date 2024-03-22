def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+106 769-858-438'
    # Output: '769'
    return input_str.split()[1][:3]

# Test the function with the provided inputs
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: '769'
print(get_first_three_numbers_after_space('+83 973-757-831'))   # Output: '973'
print(get_first_three_numbers_after_space('+62 647-787-775'))   # Output: '647'
print(get_first_three_numbers_after_space('+172 027-507-632'))  # Output: '027'
print(get_first_three_numbers_after_space('+72 001-050-856'))   # Output: '001'
print(get_first_three_numbers_after_space('+95 310-537-401'))   # Output: '310'
print(get_first_three_numbers_after_space('+6 775-969-238'))    # Output: '775'
print(get_first_three_numbers_after_space('+174 594-539-946'))  # Output: '594'
print(get_first_three_numbers_after_space('+155 927-275-860'))  # Output: '927'
print(get_first_three_numbers_after_space('+167 405-461-331'))  # Output: '405'
