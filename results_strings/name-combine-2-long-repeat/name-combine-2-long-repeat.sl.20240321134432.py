def format_names(inputs):
    first_name = inputs[0]
    last_name = inputs[1]
    output = f"{first_name} {last_name[0]}."
    return output

# Prompt: return the first input, followed by a space, and then the the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.
