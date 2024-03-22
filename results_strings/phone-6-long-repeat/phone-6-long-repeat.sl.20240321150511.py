def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+45 095-746-635'
    # Output: '095'
    
    # Split the input string by space
    split_input = input_str.split()
    
    # Get the second part of the split input
    second_part = split_input[1]
    
    # Extract the first three characters from the second part
    output = second_part[:3]
    
    return output

# Test the function with the provided inputs
print(get_first_three_numbers_after_space('+45 095-746-635'))  # Output: '095'
print(get_first_three_numbers_after_space('+161 233-981-513'))  # Output: '233'
print(get_first_three_numbers_after_space('+33 547-051-264'))  # Output: '547'
