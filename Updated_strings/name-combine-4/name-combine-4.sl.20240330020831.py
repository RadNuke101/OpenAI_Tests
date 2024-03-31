# Start time: 2024-03-30 02:17:17.328570
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period, and given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Input: ['Launa', 'Withers']
# Output: Withers, L.
# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period

def format_name(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        first_name = input_list[0]
        last_name = input_list[1]
        
        formatted_name = last_name + ', ' + first_name[0] + '.'
        
        return formatted_name
    except (IndexError, ValueError) as e:
        return str(e)

# Test cases
print(format_name(['Launa', 'Withers']))  # Output: Withers, L.
print(format_name(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_name(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_name(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_name(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
print(format_name(['John']))  # Output: Input list must contain exactly 2 elements
print(format_name(['John', 'Doe', 'Smith']))  # Output: Input list must contain exactly 2 elements

# End time: 2024-03-30 02:17:22.881706
# Elapsed time in seconds: 5.552993586999946