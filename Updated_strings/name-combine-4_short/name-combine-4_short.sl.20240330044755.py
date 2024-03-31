# Start time: 2024-03-30 04:59:10.636235
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
        
        if any(len(item) == 0 for item in input_data):
            raise ValueError("Input elements should not be empty strings")
        
        output = input_data[1] + ', ' + input_data[0][0].upper() + '.'
        return output
    except ValueError as ve:
        return str(ve)

# Test cases
print(format_output(['Launa', 'Withers']))  # Output: Withers, L.
print(format_output(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_output(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_output(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_output(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
print(format_output(['John']))  # Output: Input should contain exactly two elements
print(format_output(['', 'Smith']))  # Output: Input elements should not be empty strings
print(format_output([1, 'Doe']))  # Output: Input elements should be strings

# End time: 2024-03-30 04:59:17.901105
# Elapsed time in seconds: 7.265040977999888