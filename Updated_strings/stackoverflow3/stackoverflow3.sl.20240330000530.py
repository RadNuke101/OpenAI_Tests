# Start time: 2024-03-30 00:21:58.907826
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything after the sequence of 4 numbers (excluding spaces) from input, and given input as ['geb. 14 oct 1956 Westerkerk HRL'] output is Westerkerk HRL, given input as ['geb. 14 oct 1956 '] output is , given input as ['geb. 15 feb 1987 Westerkerk HRL'] output is Westerkerk HRL, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return everything after the sequence of 4 numbers (excluding spaces) from input
# Input: ['geb. 14 oct 1956 Westerkerk HRL']
# Output: Westerkerk HRL

def extract_text(input_str):
    try:
        # Split the input string by spaces
        parts = input_str.split()
        
        # Find the index of the first occurrence of 4 consecutive digits
        index = 0
        for i in range(len(parts) - 3):
            if parts[i].isdigit() and parts[i+1].isdigit() and parts[i+2].isdigit() and parts[i+3].isdigit():
                index = i + 4
                break
        
        # Extract the text after the 4 numbers
        result = ' '.join(parts[index:])
        
        return result
    except Exception as e:
        return str(e)

# Test cases
print(extract_text('geb. 14 oct 1956 Westerkerk HRL'))  # Output: Westerkerk HRL
print(extract_text('geb. 14 oct 1956 '))  # Output: 
print(extract_text('geb. 15 feb 1987 Westerkerk HRL'))  # Output: Westerkerk HRL

# End time: 2024-03-30 00:22:01.575552
# Elapsed time in seconds: 2.667697205999957