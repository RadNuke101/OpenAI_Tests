# Start time: 2024-03-29 23:44:43.851462
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the last word/phrase from input, and given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the last word/phrase from input
# Input: ['india china japan']
# Output: india china

def remove_last_word(input_str):
    try:
        input_str = input_str.strip()
        words = input_str.split()
        output_str = ' '.join(words[:-1])
        return output_str
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
print(remove_last_word('india china japan'))  # Output: india china
print(remove_last_word('indonesia korea'))     # Output: indonesia
print(remove_last_word('hello world'))         # Output: hello
print(remove_last_word('single'))              # Output: 


# End time: 2024-03-29 23:44:46.786848
# Elapsed time in seconds: 2.935300252999923