# Start time: 2024-03-30 00:17:46.897781
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return "Dr. " and the first input after
# Input: ['Nancy FreeHafer'] -> Output: Dr. Nancy
# Input: ['Andrew Cencici'] -> Output: Dr. Andrew
# Input: ['Jan Kotas'] -> Output: Dr. Jan
# Input: ['Mariya Sergienko'] -> Output: Dr. Mariya

def generate_doctor_name(input_list):
    try:
        # Extract the first name from the input list
        first_name = input_list[0].split()[0]
        return "Dr. " + first_name
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(generate_doctor_name(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(generate_doctor_name(['Andrew Cencici']))  # Output: Dr. Andrew
print(generate_doctor_name(['Jan Kotas']))  # Output: Dr. Jan
print(generate_doctor_name(['Mariya Sergienko']))  # Output: Dr. Mariya
print(generate_doctor_name([]))  # Output: Invalid input
print(generate_doctor_name(['John Doe', 'Jane Smith']))  # Output: Dr. John

# End time: 2024-03-30 00:17:50.447752
# Elapsed time in seconds: 3.5499512149999646