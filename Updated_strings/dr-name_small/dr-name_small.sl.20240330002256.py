# Start time: 2024-03-30 00:35:53.940791
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return "Dr. " and the first input after, and given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return "Dr. "
# Input: ['Nancy FreeHafer']
# Output: Dr. Nancy

def generate_title(input_str):
    try:
        name = input_str[0].split()[0]
        return "Dr. " + name
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(generate_title(['Nancy FreeHafer']))  # Output: Dr. Nancy
print(generate_title(['Andrew Cencici']))   # Output: Dr. Andrew
print(generate_title(['Jan Kotas']))        # Output: Dr. Jan
print(generate_title(['Mariya Sergienko'])) # Output: Dr. Mariya
print(generate_title([]))                    # Output: Invalid input
print(generate_title(['John', 'Doe']))       # Output: Invalid input

# End time: 2024-03-30 00:35:56.435237
# Elapsed time in seconds: 2.4944249519999175