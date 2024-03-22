def format_names(input):
    name1, name2 = input.split(', ')
    return f"{name2}, {name1[0]}."
    
# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: "Launa, Withers"
# Output: "Withers, L."
