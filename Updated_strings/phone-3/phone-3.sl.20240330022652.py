# Start time: 2024-03-30 02:29:57.019816
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space, and given input as ['938-242-504'] output is (938) 242-504, given input as ['308-916-545'] output is (308) 916-545, given input as ['623-599-749'] output is (623) 599-749, given input as ['981-424-843'] output is (981) 424-843, given input as ['118-980-214'] output is (118) 980-214, given input as ['244-655-094'] output is (244) 655-094, given input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: '938-242-504'
# Output: (938) 242-504

def format_phone_number(input_str):
    try:
        # Split the input string by "-"
        parts = input_str.split("-")
        
        # Extract the first three numbers and format them with parentheses
        first_part = "(" + parts[0] + ")"
        
        # Remove the first "-" and replace it with a space
        formatted_number = first_part + " " + parts[1] + "-" + parts[2]
        
        return formatted_number
    except Exception as e:
        return "Error: Invalid input format"

# Test cases
print(format_phone_number('938-242-504'))  # Output: (938) 242-504
print(format_phone_number('308-916-545'))  # Output: (308) 916-545
print(format_phone_number('623-599-749'))  # Output: (623) 599-749
print(format_phone_number('981-424-843'))  # Output: (981) 424-843
print(format_phone_number('118-980-214'))  # Output: (118) 980-214
print(format_phone_number('244-655-094'))  # Output: (244) 655-094
print(format_phone_number('830-941-991'))  # Output: (830) 941-991

# End time: 2024-03-30 02:30:01.019441
# Elapsed time in seconds: 3.9995338230000925