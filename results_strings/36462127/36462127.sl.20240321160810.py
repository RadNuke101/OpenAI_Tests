# Prompt: return the letters after the last "/"
# Input: ['ABCDE/FGHI/JKL/MNOPQR']
# Output: MNOPQR
# Input: ['A/ABCDE/FGHI/JKL']
# Output: JKL

def letters_after_last_slash(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test the function with the provided inputs
print(letters_after_last_slash('ABCDE/FGHI/JKL/MNOPQR'))  # Output: MNOPQR
print(letters_after_last_slash('A/ABCDE/FGHI/JKL'))      # Output: JKL
