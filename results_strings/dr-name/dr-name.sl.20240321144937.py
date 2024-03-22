# Prompt: return "Dr. "
# Input: ['Nancy FreeHafer']
# Output: Dr. Nancy

def return_dr_name(input_str):
    name = input_str.split()[0]
    return "Dr. " + name

# Test cases
print(return_dr_name('Nancy FreeHafer'))  # Output: Dr. Nancy
print(return_dr_name('Andrew Cencici'))    # Output: Dr. Andrew
print(return_dr_name('Jan Kotas'))         # Output: Dr. Jan
print(return_dr_name('Mariya Sergienko'))  # Output: Dr. Mariya
