def get_first_word(input_str):
    return input_str.split()[0]

# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer'] Output: Nancy
# Input: ['Andrew Cencici'] Output: Andrew
# Input: ['Jan Kotas'] Output: Jan
# Input: ['Mariya Sergienko'] Output: Mariya
# Input: ['Launa Withers'] Output: Launa
# Input: ['Lakenya Edison'] Output: Lakenya
# ... (additional inputs and outputs provided in the prompt)

# Test the function with one of the inputs
input_str = 'Nancy FreeHafer'
output_str = get_first_word(input_str)
print(output_str)  # Output: Nancy
