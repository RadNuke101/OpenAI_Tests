# Prompt: return "Dr. "
# Input: ['Nancy FreeHafer']
# Output: Dr. Nancy
# Input: ['Andrew Cencici']
# Output: Dr. Andrew
# Input: ['Jan Kotas']
# Output: Dr. Jan
# Input: ['Mariya Sergienko']
# Output: Dr. Mariya

def add_title(input_name):
    name = input_name[0].split()
    return "Dr. " + name[0]

# Test the function with the provided inputs
print(add_title(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(add_title(['Andrew Cencici']))  # Output: Dr. Andrew
print(add_title(['Jan Kotas']))  # Output: Dr. Jan
print(add_title(['Mariya Sergienko']))  # Output: Dr. Mariya
