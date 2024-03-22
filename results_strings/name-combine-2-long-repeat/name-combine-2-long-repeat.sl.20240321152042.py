def format_names(input):
    first_name = input[0]
    last_name = input[1]
    output = f"{first_name} {last_name[0]}."
    return output

# Prompt: return the first input, followed by a space, and then the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.
