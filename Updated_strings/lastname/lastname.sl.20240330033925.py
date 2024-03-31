# Start time: 2024-03-30 03:47:44.448675
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and given input as ['Nancy FreeHafer'] output is FreeHafer, given input as ['Andrew Cencici'] output is Cencici, given input as ['Jan Kotas'] output is Kotas, given input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second word of the inputted phrase
# Input: ['Nancy FreeHafer'] 
# Output: FreeHafer

def get_second_word(input_phrase):
    try:
        # Extract the input phrase from the list
        input_phrase = input_phrase[0]
        
        # Split the input phrase into words
        words = input_phrase.split()
        
        # Return the second word
        return words[1]
    
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(get_second_word(['Nancy FreeHafer']))  # Output: FreeHafer
print(get_second_word(['Andrew Cencici']))    # Output: Cencici
print(get_second_word(['Jan Kotas']))         # Output: Kotas
print(get_second_word(['Mariya Sergienko']))  # Output: Sergienko

# End time: 2024-03-30 03:47:50.234139
# Elapsed time in seconds: 5.785271349999675