# Prompt: return the letters after the last "/"
# Input: ['ABCDE/FGHI/JKL/MNOPQR'] Output: MNOPQR
# Input: ['A/ABCDE/FGHI/JKL'] Output: JKL

def get_letters_after_last_slash(input_str):
    parts = input_str.split('/')
    return parts[-1]

# Test cases
print(get_letters_after_last_slash('ABCDE/FGHI/JKL/MNOPQR'))  # Output: MNOPQR
print(get_letters_after_last_slash('A/ABCDE/FGHI/JKL'))      # Output: JKL
