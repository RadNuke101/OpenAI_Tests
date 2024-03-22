def get_year(input_str):
    input_list = input_str.split()
    for item in input_list:
        if item.isdigit() and len(item) == 4:
            return item

# Prompt: return the sequence of 4 numbers (excluding spaces) from input
# Input: ['April 1 1799']
# Output: 1799
print(get_year('April 1 1799'))  # Output: 1799
