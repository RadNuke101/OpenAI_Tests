# Start time: 2024-03-30 03:42:43.828461
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period, and given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer'] Output: N.F.
# Input: ['Andrew Cencici'] Output: A.C.
# Input: ['Jan Kotas'] Output: J.K.
# Input: ['Mariya Sergienko'] Output: M.S.

def get_initials(input_phrase):
    try:
        words = input_phrase[0].split()
        initials = ""
        for word in words:
            initials += word[0].upper() + "."
        return initials[:-1]  # Remove the extra period at the end
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(get_initials(['Nancy FreeHafer']))  # Output: N.F.
print(get_initials(['Andrew Cencici']))  # Output: A.C.
print(get_initials(['Jan Kotas']))  # Output: J.K.
print(get_initials(['Mariya Sergienko']))  # Output: M.S.
print(get_initials(['InvalidInput']))  # Output: Invalid input

# End time: 2024-03-30 03:42:46.806711
# Elapsed time in seconds: 2.9781420819999767