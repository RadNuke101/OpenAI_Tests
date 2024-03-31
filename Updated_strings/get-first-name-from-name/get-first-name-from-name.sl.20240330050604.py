# Start time: 2024-03-30 05:11:57.054401
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, and given input as ['Susan Ann Chang'] output is Susan, given input as ['Ayako Tanaka'] output is Ayako, given input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first word of the inputted phrase
# Input: ['Susan Ann Chang']
# Output: Susan

def get_first_word(input_phrase):
    try:
        # Extract the first word from the input phrase
        first_word = input_phrase.split()[0]
        return first_word
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(get_first_word('Susan Ann Chang'))  # Output: Susan
print(get_first_word('Ayako Tanaka'))      # Output: Ayako
print(get_first_word('Bobby T. smth'))     # Output: Bobby

# End time: 2024-03-30 05:11:59.197317
# Elapsed time in seconds: 2.142905721997522