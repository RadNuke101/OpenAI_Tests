# Prompt: return "Dr. " and the first input after
# Input: ['Nancy FreeHafer'] Output: Dr. Nancy
# Input: ['Andrew Cencici'] Output: Dr. Andrew
# Input: ['Jan Kotas'] Output: Dr. Jan
# Input: ['Mariya Sergienko'] Output: Dr. Mariya

def add_title(input_str):
    name = input_str.split()[0]
    return "Dr. " + name

# Test cases
print(add_title('Nancy FreeHafer'))  # Output: Dr. Nancy
print(add_title('Andrew Cencici'))   # Output: Dr. Andrew
print(add_title('Jan Kotas'))        # Output: Dr. Jan
print(add_title('Mariya Sergienko')) # Output: Dr. Mariya
