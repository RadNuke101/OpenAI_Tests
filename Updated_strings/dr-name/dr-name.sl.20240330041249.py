# Start time: 2024-03-30 04:19:37.933332
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return "Dr. "
# Input: ['Nancy FreeHafer']
# Output: Dr. Nancy

def generate_title(input_str):
    try:
        # Extracting the first name from the input string
        first_name = input_str.split()[0]
        return "Dr. " + first_name
    except:
        return "Invalid input"

# Test cases
print(generate_title('Nancy FreeHafer'))  # Output: Dr. Nancy
print(generate_title('Andrew Cencici'))    # Output: Dr. Andrew
print(generate_title('Jan Kotas'))         # Output: Dr. Jan
print(generate_title('Mariya Sergienko'))  # Output: Dr. Mariya

# End time: 2024-03-30 04:19:40.728747
# Elapsed time in seconds: 2.7953287769996678