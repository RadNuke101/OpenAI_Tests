# Prompt: return the letters after the last "/"
# Input: ['ABCDE/FGHI/JKL/MNOPQR'] Output: MNOPQR
# Input: ['A/ABCDE/FGHI/JKL'] Output: JKL

def letters_after_last_slash(input_list):
    input_str = input_list[0]  # Extract the string from the list
    parts = input_str.split('/')  # Split the string by "/"
    output = parts[-1]  # Get the last part after splitting
    return output

# Test cases
print(letters_after_last_slash(['ABCDE/FGHI/JKL/MNOPQR']))  # Output: MNOPQR
print(letters_after_last_slash(['A/ABCDE/FGHI/JKL']))  # Output: JKL
