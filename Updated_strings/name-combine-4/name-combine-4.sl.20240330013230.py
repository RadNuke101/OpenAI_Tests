# Start time: 2024-03-30 01:41:32.654072
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period, and given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Input: 'Launa', 'Withers'
# Output: 'Withers, L.'

def format_names(input1, input2):
    try:
        output = input2 + ', ' + input1[0] + '.'
        return output
    except (IndexError, TypeError) as e:
        print("Invalid input format. Please provide two strings.")
        return None

# Test cases
print(format_names('Launa', 'Withers'))  # Output: 'Withers, L.'
print(format_names('Lakenya', 'Edison'))  # Output: 'Edison, L.'
print(format_names('Brendan', 'Hage'))  # Output: 'Hage, B.'
print(format_names('Bradford', 'Lango'))  # Output: 'Lango, B.'
print(format_names('Rudolf', 'Akiyama'))  # Output: 'Akiyama, R.'
print(format_names(['Invalid', 'Input']))  # Output: None

# End time: 2024-03-30 01:41:34.364032
# Elapsed time in seconds: 1.7099284359992453