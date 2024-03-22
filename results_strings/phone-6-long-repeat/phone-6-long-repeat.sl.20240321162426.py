def get_first_three_numbers_after_space(input_str):
    # Prompt: return first three numbers after the first space in input
    # Input: '+45 095-746-635'
    # Output: '095'
    
    # Split the input string by space
    parts = input_str.split()
    
    # Get the second part (numbers after the space)
    numbers_after_space = parts[1]
    
    # Extract the first three numbers
    first_three_numbers = numbers_after_space[:3]
    
    return first_three_numbers

# Test the function with the given inputs
print(get_first_three_numbers_after_space('+45 095-746-635'))  # Output: '095'
print(get_first_three_numbers_after_space('+161 233-981-513'))  # Output: '233'
print(get_first_three_numbers_after_space('+33 547-051-264'))  # Output: '547'
