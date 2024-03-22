# Prompt: return "Dr. "
# Given input as ['Nancy FreeHafer'] output is Dr. Nancy
# Given input as ['Andrew Cencici'] output is Dr. Andrew
# Given input as ['Jan Kotas'] output is Dr. Jan
# Given input as ['Mariya Sergienko'] output is Dr. Mariya

def add_title(input_name):
    name = input_name[0].split()
    return "Dr. " + name[0]

# Test cases
print(add_title(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(add_title(['Andrew Cencici']))   # Output: Dr. Andrew
print(add_title(['Jan Kotas']))        # Output: Dr. Jan
print(add_title(['Mariya Sergienko']))  # Output: Dr. Mariya
