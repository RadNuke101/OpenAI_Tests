# Start time: 2024-03-29 23:51:08.948167
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, and given input as ['Nancy FreeHafer'] output is Nancy, given input as ['Andrew Cencici'] output is Andrew, given input as ['Jan Kotas'] output is Jan, given input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first word of the inputted phrase
# Input: ['Nancy FreeHafer']  Output: Nancy
# Input: ['Andrew Cencici']  Output: Andrew
# Input: ['Jan Kotas']  Output: Jan
# Input: ['Mariya Sergienko']  Output: Mariya

def get_first_word(input_phrase):
    try:
        # Extract the first word from the input phrase
        first_word = input_phrase[0].split()[0]
        return first_word
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(get_first_word(['Nancy FreeHafer']))  # Output: Nancy
print(get_first_word(['Andrew Cencici']))  # Output: Andrew
print(get_first_word(['Jan Kotas']))  # Output: Jan
print(get_first_word(['Mariya Sergienko']))  # Output: Mariya

# End time: 2024-03-29 23:51:12.799584
# Elapsed time in seconds: 3.851301461000048