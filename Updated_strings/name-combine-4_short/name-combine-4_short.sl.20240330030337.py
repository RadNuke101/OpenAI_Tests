# Start time: 2024-03-30 03:14:48.508836
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period, and given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_output(input_data):
    try:
        if len(input_data) != 2:
            raise ValueError("Input should contain exactly two elements")
        
        if not all(isinstance(item, str) for item in input_data):
            raise ValueError("Input elements should be strings")
        
        if not all(item.isalpha() for item in input_data):
            raise ValueError("Input elements should only contain alphabetic characters")
        
        first_name = input_data[0]
        last_name = input_data[1]
        
        formatted_output = f"{last_name}, {first_name[0].upper()}."
        
        return formatted_output
    except ValueError as ve:
        return f"Error: {ve}"

# Test cases
print(format_output(['Launa', 'Withers']))  # Output: Withers, L.
print(format_output(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_output(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_output(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_output(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
print(format_output(['John']))  # Output: Error: Input should contain exactly two elements
print(format_output(['123', 'Smith']))  # Output: Error: Input elements should only contain alphabetic characters

# End time: 2024-03-30 03:14:53.364603
# Elapsed time in seconds: 4.855630488000315