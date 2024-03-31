# Start time: 2024-03-30 02:39:03.216698
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first input, followed by a period and a space, and then the second input, and given input as ['Launa', 'Withers'] output is L. Withers, given input as ['Lakenya', 'Edison'] output is L. Edison, given input as ['Brendan', 'Hage'] output is B. Hage, given input as ['Bradford', 'Lango'] output is B. Lango, given input as ['Rudolf', 'Akiyama'] output is R. Akiyama, given input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers'] => Output: L. Withers
# Input: ['Lakenya', 'Edison'] => Output: L. Edison
# Input: ['Brendan', 'Hage'] => Output: B. Hage
# Input: ['Bradford', 'Lango'] => Output: B. Lango
# Input: ['Rudolf', 'Akiyama'] => Output: R. Akiyama
# Input: ['Lara', 'Constable'] => Output: L. Constable

def format_name(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        first_letter = input_list[0][0]
        formatted_name = f"{first_letter}. {input_list[1]}"
        
        return formatted_name
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")
        return None

# Test cases
print(format_name(['Launa', 'Withers']))  # Output: L. Withers
print(format_name(['Lakenya', 'Edison']))  # Output: L. Edison
print(format_name(['Brendan', 'Hage']))  # Output: B. Hage
print(format_name(['Bradford', 'Lango']))  # Output: B. Lango
print(format_name(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
print(format_name(['Lara', 'Constable']))  # Output: L. Constable
print(format_name(['John']))  # Error: Input list must contain exactly 2 elements
print(format_name('Invalid input'))  # Error: 'str' object is not subscriptable

# End time: 2024-03-30 02:39:07.214552
# Elapsed time in seconds: 3.997765915000855