# Start time: 2024-03-30 03:17:05.863038
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last word/phrase from input, and given input as ['Sarah Jane Jones'] output is Jones, given input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return last word/phrase from input
# Input: ['Sarah Jane Jones'] 
# Output: Jones
# Input: ['Bob Jane Smithfield'] 
# Output: Smithfield

def get_last_word(input_str):
    try:
        words = input_str.split()
        last_word = words[-1]
        return last_word
    except Exception as e:
        print("Error: ", e)

# Test cases
print(get_last_word('Sarah Jane Jones'))  # Output: Jones
print(get_last_word('Bob Jane Smithfield'))  # Output: Smithfield

# End time: 2024-03-30 03:17:07.099722
# Elapsed time in seconds: 1.236650753999129