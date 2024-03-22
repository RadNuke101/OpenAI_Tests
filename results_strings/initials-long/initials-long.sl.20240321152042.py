def get_initials(input_str):
    words = input_str.split()
    initials = ""
    for word in words:
        initials += word[0].upper() + "."
    return initials[:-1]

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer'] 
# Output: N.F.

input_str = 'Nancy FreeHafer'
print(get_initials(input_str))
