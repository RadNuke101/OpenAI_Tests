# Start time: 2024-03-30 04:46:44.467610
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the last word of the inputted phrase, and given input as ['focus on one thing at a time'] output is time, given input as ['premature opt is the root of all evil'] output is evil, given input as ['where is life'] output is life, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the last word of the inputted phrase

def get_last_word(input_phrase):
    try:
        words = input_phrase.split()
        last_word = words[-1]
        return last_word
    except:
        return "Invalid input"

# Test cases
print(get_last_word('focus on one thing at a time'))  # Output: time
print(get_last_word('premature opt is the root of all evil'))  # Output: evil
print(get_last_word('where is life'))  # Output: life

# End time: 2024-03-30 04:46:47.011487
# Elapsed time in seconds: 2.543873425001948