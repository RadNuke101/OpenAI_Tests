# Start time: 2024-03-30 03:15:58.999553
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return "Dr. " and the first input after
# Input: ['Nancy FreeHafer'] Output: Dr. Nancy
# Input: ['Andrew Cencici'] Output: Dr. Andrew
# Input: ['Jan Kotas'] Output: Dr. Jan
# Input: ['Mariya Sergienko'] Output: Dr. Mariya

def get_doctor_name(input_list):
    try:
        name = input_list[0].split()[0]
        return "Dr. " + name
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(get_doctor_name(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(get_doctor_name(['Andrew Cencici']))  # Output: Dr. Andrew
print(get_doctor_name(['Jan Kotas']))  # Output: Dr. Jan
print(get_doctor_name(['Mariya Sergienko']))  # Output: Dr. Mariya
print(get_doctor_name(['John']))  # Output: Dr. John
print(get_doctor_name([]))  # Output: Invalid input format

# End time: 2024-03-30 03:16:03.827065
# Elapsed time in seconds: 4.827377662000799