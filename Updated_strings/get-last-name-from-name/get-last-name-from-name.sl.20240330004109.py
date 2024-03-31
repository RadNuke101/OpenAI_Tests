# Start time: 2024-03-30 00:54:16.710186
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and given input as ['Park Kim'] output is Kim, given input as ['Lee Kim'] output is Kim, given input as ['Kim Lee'] output is Lee, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second word of the inputted phrase
# Input: ['Park Kim'] 
# Output: Kim
# Input: ['Lee Kim'] 
# Output: Kim
# Input: ['Kim Lee'] 
# Output: Lee

def get_second_word(input_phrase):
    try:
        # Split the input phrase by space and get the second word
        second_word = input_phrase.split()[1]
        return second_word
    except IndexError:
        return "Input phrase does not have a second word"

# Test cases
print(get_second_word('Park Kim'))  # Output: Kim
print(get_second_word('Lee Kim'))   # Output: Kim
print(get_second_word('Kim Lee'))   # Output: Lee

# End time: 2024-03-30 00:54:19.114672
# Elapsed time in seconds: 2.4044282570002906