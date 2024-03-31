# Start time: 2024-03-30 03:25:48.147425
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if inputted phrase has more than one word, return the first word, else return nothing, and given input as ['The quick brown fox.'] output is The, given input as ['quick brown fox.'] output is quick, given input as ['fox'] output is , , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if inputted phrase has more than one word, return the first word, else return nothing
# Input: 'The quick brown fox.' Output: 'The'
# Input: 'quick brown fox.' Output: 'quick'
# Input: 'fox' Output: ''

def get_first_word(input_str):
    try:
        words = input_str.split()
        if len(words) > 1:
            return words[0]
        else:
            return ''
    except:
        return ''

# Test cases
print(get_first_word('The quick brown fox.'))  # Output: 'The'
print(get_first_word('quick brown fox.'))       # Output: 'quick'
print(get_first_word('fox'))                     # Output: ''

# End time: 2024-03-30 03:25:55.835581
# Elapsed time in seconds: 7.687981883998873