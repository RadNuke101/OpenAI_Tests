# Prompt: return the letters after the last "/"
# Input: ['ABCDE/FGHI/JKL/MNOPQR']
# Output: MNOPQR

def get_letters_after_last_slash(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test the function with the provided inputs
input_1 = 'ABCDE/FGHI/JKL/MNOPQR'
output_1 = get_letters_after_last_slash(input_1)
print(output_1)  # Output should be MNOPQR

input_2 = 'A/ABCDE/FGHI/JKL'
output_2 = get_letters_after_last_slash(input_2)
print(output_2)  # Output should be JKL
