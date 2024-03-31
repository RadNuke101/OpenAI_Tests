# Start time: 2024-03-30 03:03:25.524354
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return second input, followed by a space, and then the first input, and given input as ['Launa', 'Withers'] output is Withers Launa, given input as ['Lakenya', 'Edison'] output is Edison Lakenya, given input as ['Brendan', 'Hage'] output is Hage Brendan, given input as ['Bradford', 'Lango'] output is Lango Bradford, given input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, given input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers'] 
# Output: Withers Launa

def reverse_names(input_str):
    try:
        # Split the input string into a list of names
        names = input_str.split()
        
        # Reverse the order of names and concatenate them with a space in between
        reversed_names = names[1] + ' ' + names[0]
        
        return reversed_names
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(reverse_names('Launa Withers'))  # Output: Withers Launa
print(reverse_names('Lakenya Edison'))  # Output: Edison Lakenya
print(reverse_names('Brendan Hage'))  # Output: Hage Brendan
print(reverse_names('Bradford Lango'))  # Output: Lango Bradford
print(reverse_names('Rudolf Akiyama'))  # Output: Akiyama Rudolf
print(reverse_names('Lara Constable'))  # Output: Constable Lara

# End time: 2024-03-30 03:03:32.287076
# Elapsed time in seconds: 6.762543638998977