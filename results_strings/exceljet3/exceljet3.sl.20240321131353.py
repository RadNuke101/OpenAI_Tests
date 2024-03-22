# Prompt: return everything after the space in the inputted expression

def extract_after_space(input_str):
    return input_str.split('= ')[1]

# Test cases
print(extract_after_space('year= 2016'))  # Output: 2016
print(extract_after_space('make= subaru'))  # Output: subaru
print(extract_after_space('model= outback wagon'))  # Output: outback wagon
print(extract_after_space('fuel economy= 25/33'))  # Output: 25/33
