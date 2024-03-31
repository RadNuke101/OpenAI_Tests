# Start time: 2024-03-30 04:41:45.856132
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period, and given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers']
# Output: Withers, L.

def format_names(inputs):
    try:
        if len(inputs) != 2:
            raise ValueError("Input should be a list of two strings")
        
        if not all(isinstance(name, str) for name in inputs):
            raise ValueError("Input elements should be strings")
        
        if len(inputs[0]) == 0 or len(inputs[1]) == 0:
            raise ValueError("Input strings should not be empty")
        
        formatted_output = inputs[1] + ', ' + inputs[0][0].upper() + '.'
        return formatted_output
    except ValueError as ve:
        return str(ve)

# Test cases
print(format_names(['Launa', 'Withers']))  # Output: Withers, L.
print(format_names(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_names(['Brendan', 'Hage']))    # Output: Hage, B.
print(format_names(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_names(['Rudolf', 'Akiyama']))   # Output: Akiyama, R.
print(format_names(['', '']))                # Output: Input strings should not be empty
print(format_names(['John']))                # Output: Input should be a list of two strings
print(format_names(['John', 123]))           # Output: Input elements should be strings

# End time: 2024-03-30 04:41:50.103152
# Elapsed time in seconds: 4.247009935999813