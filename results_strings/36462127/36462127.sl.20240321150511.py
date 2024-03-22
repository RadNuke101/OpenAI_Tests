# Prompt: return the letters after the last "/"
# Input: ['ABCDE/FGHI/JKL/MNOPQR']
# Output: MNOPQR

def get_letters_after_last_slash(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test the function with the provided inputs
input1 = 'ABCDE/FGHI/JKL/MNOPQR'
output1 = get_letters_after_last_slash(input1)
print(output1)  # Output: MNOPQR

input2 = 'A/ABCDE/FGHI/JKL'
output2 = get_letters_after_last_slash(input2)
print(output2)  # Output: JKL
