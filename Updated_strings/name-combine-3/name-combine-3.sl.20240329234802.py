# Start time: 2024-03-29 23:58:13.443416
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first input, followed by a period and a space, and then the second input, and given input as ['Launa', 'Withers'] output is L. Withers, given input as ['Lakenya', 'Edison'] output is L. Edison, given input as ['Brendan', 'Hage'] output is B. Hage, given input as ['Bradford', 'Lango'] output is B. Lango, given input as ['Rudolf', 'Akiyama'] output is R. Akiyama, given input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers'] 
# Output: L. Withers

def get_formatted_output(input_str):
    try:
        # Convert input string to list
        input_list = input_str.split()
        
        # Extract first letter of the first input
        first_letter = input_list[0][0]
        
        # Format the output
        output = f"{first_letter}. {input_list[1]}"
        
        return output
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(get_formatted_output('Launa Withers'))  # Output: L. Withers
print(get_formatted_output('Lakenya Edison'))  # Output: L. Edison
print(get_formatted_output('Brendan Hage'))  # Output: B. Hage
print(get_formatted_output('Bradford Lango'))  # Output: B. Lango
print(get_formatted_output('Rudolf Akiyama'))  # Output: R. Akiyama
print(get_formatted_output('Lara Constable'))  # Output: L. Constable

# End time: 2024-03-29 23:58:18.565365
# Elapsed time in seconds: 5.121790132999877