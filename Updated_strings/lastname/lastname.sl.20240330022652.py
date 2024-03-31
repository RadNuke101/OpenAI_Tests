# Start time: 2024-03-30 02:37:16.228632
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and given input as ['Nancy FreeHafer'] output is FreeHafer, given input as ['Andrew Cencici'] output is Cencici, given input as ['Jan Kotas'] output is Kotas, given input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second word of the inputted phrase
# Input: 'Nancy FreeHafer', Output: 'FreeHafer'
# Input: 'Andrew Cencici', Output: 'Cencici'
# Input: 'Jan Kotas', Output: 'Kotas'
# Input: 'Mariya Sergienko', Output: 'Sergienko'

def get_second_word(input_phrase):
    try:
        words = input_phrase.split()
        if len(words) >= 2:
            return words[1]
        else:
            return "Input phrase does not contain a second word"
    except:
        return "Error processing input"

# Test cases
print(get_second_word('Nancy FreeHafer'))  # Output: FreeHafer
print(get_second_word('Andrew Cencici'))    # Output: Cencici
print(get_second_word('Jan Kotas'))         # Output: Kotas
print(get_second_word('Mariya Sergienko'))  # Output: Sergienko

# End time: 2024-03-30 02:37:19.203933
# Elapsed time in seconds: 2.975345250999453