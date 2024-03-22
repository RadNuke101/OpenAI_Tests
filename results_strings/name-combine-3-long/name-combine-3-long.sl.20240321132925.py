def first_letter_period(input_str):
    input_list = input_str.split(', ')
    first_letter = input_list[0][0]
    output = first_letter + '. ' + input_list[1]
    return output

# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: "Jenee, Pannell"
# Output: "J. Pannell"

input_str = "Jenee, Pannell"
print(first_letter_period(input_str))
