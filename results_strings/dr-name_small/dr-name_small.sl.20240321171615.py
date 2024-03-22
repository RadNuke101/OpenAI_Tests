# Prompt: return "Dr. "
# Input: ['Nancy FreeHafer']
# Output: Dr. Nancy
# Input: ['Andrew Cencici']
# Output: Dr. Andrew
# Input: ['Jan Kotas']
# Output: Dr. Jan
# Input: ['Mariya Sergienko']
# Output: Dr. Mariya

def generate_doctor_name(input_str):
    name = input_str[0].split()[0]
    return "Dr. " + name

# Test cases
print(generate_doctor_name(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(generate_doctor_name(['Andrew Cencici']))   # Output: Dr. Andrew
print(generate_doctor_name(['Jan Kotas']))        # Output: Dr. Jan
print(generate_doctor_name(['Mariya Sergienko'])) # Output: Dr. Mariya
