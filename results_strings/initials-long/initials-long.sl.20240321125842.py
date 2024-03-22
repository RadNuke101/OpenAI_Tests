def get_initials(input_str):
    words = input_str.split()
    initials = words[0][0] + '.' + words[1][0] + '.'
    return initials

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer']
# Output: N.F.

input_str = 'Nancy FreeHafer'
print(get_initials(input_str))  # Output: N.F.
