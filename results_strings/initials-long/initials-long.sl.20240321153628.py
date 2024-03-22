def get_initials(input_str):
    words = input_str.split()
    initials = [word[0].upper() for word in words]
    return '.'.join(initials) + '.'

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer']
# Output: N.F.

# Input: ['Andrew Cencici']
# Output: A.C.

# Input: ['Jan Kotas']
# Output: J.K.

# Example usage:
input_str = 'Nancy FreeHafer'
print(get_initials(input_str))  # Output: N.F.
