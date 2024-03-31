# Start time: 2024-03-30 04:58:59.884367
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first input, followed by a period and a space, and then the second input, and given input as ['Launa', 'Withers'] output is L. Withers, given input as ['Lakenya', 'Edison'] output is L. Edison, given input as ['Brendan', 'Hage'] output is B. Hage, given input as ['Bradford', 'Lango'] output is B. Lango, given input as ['Rudolf', 'Akiyama'] output is R. Akiyama, given input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers'] 
# Output: L. Withers

def process_input(input_data):
    try:
        if isinstance(input_data, list) and len(input_data) == 2:
            first_name = input_data[0]
            last_name = input_data[1]
            if isinstance(first_name, str) and isinstance(last_name, str):
                return f"{first_name[0]}. {last_name}"
            else:
                raise ValueError("Input names must be strings")
        else:
            raise ValueError("Input must be a list of two strings")
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(process_input(['Launa', 'Withers']))  # Output: L. Withers
print(process_input(['Lakenya', 'Edison']))  # Output: L. Edison
print(process_input(['Brendan', 'Hage']))  # Output: B. Hage
print(process_input(['Bradford', 'Lango']))  # Output: B. Lango
print(process_input(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
print(process_input(['Lara', 'Constable']))  # Output: L. Constable

# End time: 2024-03-30 04:59:06.011107
# Elapsed time in seconds: 6.126874613000837