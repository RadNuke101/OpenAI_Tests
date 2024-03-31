# Start time: 2024-03-30 00:47:31.889362
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first letter of first word, followed by a space, and then the second word, and given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return first letter of first word, followed by a space, and then the second word
# Input: ['John Doe'] Output: J Doe
# Input: ['Mayur Naik'] Output: M Naik
# Input: ['Nimit Singh'] Output: N Singh

def process_input(input_str):
    try:
        # Extracting the first word and second word from the input string
        words = input_str.split()
        first_letter = words[0][0]
        second_word = words[1]
        
        return first_letter + " " + second_word
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(process_input('John Doe'))  # Output: J Doe
print(process_input('Mayur Naik'))  # Output: M Naik
print(process_input('Nimit Singh'))  # Output: N Singh

# End time: 2024-03-30 00:47:35.031937
# Elapsed time in seconds: 3.1425108049998016