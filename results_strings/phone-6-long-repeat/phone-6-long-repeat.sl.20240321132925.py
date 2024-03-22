def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Given input as ['+106 769-858-438'] output is 769
    # Given input as ['+83 973-757-831'] output is 973
    # Given input as ['+62 647-787-775'] output is 647
    # Given input as ['+172 027-507-632'] output is 027
    # Given input as ['+72 001-050-856'] output is 001
    # Given input as ['+95 310-537-401'] output is 310
    space_index = input_str.index(' ')
    numbers_after_space = input_str[space_index+1:space_index+4]
    return numbers_after_space

# Test cases
print(get_first_three_numbers_after_space('+106 769-858-438'))  # Output: 769
print(get_first_three_numbers_after_space('+83 973-757-831'))  # Output: 973
print(get_first_three_numbers_after_space('+62 647-787-775'))  # Output: 647
print(get_first_three_numbers_after_space('+172 027-507-632'))  # Output: 027
print(get_first_three_numbers_after_space('+72 001-050-856'))  # Output: 001
print(get_first_three_numbers_after_space('+95 310-537-401'))  # Output: 310
