# Start time: 2024-03-30 02:52:39.253111
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return "Dr. "
# Input: ['Nancy FreeHafer']
# Output: Dr. Nancy

def get_doctor_name(input_str):
    try:
        name = input_str[0].split()[0]
        return "Dr. " + name
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(get_doctor_name(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(get_doctor_name(['Andrew Cencici']))   # Output: Dr. Andrew
print(get_doctor_name(['Jan Kotas']))         # Output: Dr. Jan
print(get_doctor_name(['Mariya Sergienko']))  # Output: Dr. Mariya

# End time: 2024-03-30 02:52:43.076974
# Elapsed time in seconds: 3.82375677500022