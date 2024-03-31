# Start time: 2024-03-30 02:04:10.706656
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last word/phrase from input, and given input as ['Sarah Jane Jones'] output is Jones, given input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return last word/phrase from input
# Input: ['Sarah Jane Jones'] 
# Output: Jones
# Input: ['Bob Jane Smithfield'] 
# Output: Smithfield

def return_last_word(input_str):
    try:
        words = input_str.split()
        last_word = words[-1]
        return last_word
    except:
        return "Invalid input"

# Test cases
print(return_last_word('Sarah Jane Jones'))  # Output: Jones
print(return_last_word('Bob Jane Smithfield'))  # Output: Smithfield
print(return_last_word('Hello World'))  # Output: World
print(return_last_word('OnlyOneWord'))  # Output: OnlyOneWord
print(return_last_word(''))  # Output: Invalid input

# End time: 2024-03-30 02:04:15.281747
# Elapsed time in seconds: 4.574963711000237