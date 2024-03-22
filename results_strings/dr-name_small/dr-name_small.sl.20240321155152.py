# Prompt: return "Dr. "
# Given input as ['Nancy FreeHafer'] output is Dr. Nancy
# Given input as ['Andrew Cencici'] output is Dr. Andrew
# Given input as ['Jan Kotas'] output is Dr. Jan
# Given input as ['Mariya Sergienko'] output is Dr. Mariya

def get_doctor_name(input_str):
    name = input_str[0].split()[0]
    return "Dr. " + name

# Test cases
print(get_doctor_name(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(get_doctor_name(['Andrew Cencici']))   # Output: Dr. Andrew
print(get_doctor_name(['Jan Kotas']))        # Output: Dr. Jan
print(get_doctor_name(['Mariya Sergienko'])) # Output: Dr. Mariya
