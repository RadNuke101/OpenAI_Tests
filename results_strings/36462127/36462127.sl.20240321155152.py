# Prompt: return the letters after the last "/"
# Input: ['ABCDE/FGHI/JKL/MNOPQR']
# Output: MNOPQR

def get_letters_after_last_slash(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test the function with the provided inputs
print(get_letters_after_last_slash('ABCDE/FGHI/JKL/MNOPQR'))  # Output: MNOPQR
print(get_letters_after_last_slash('A/ABCDE/FGHI/JKL'))      # Output: JKL
