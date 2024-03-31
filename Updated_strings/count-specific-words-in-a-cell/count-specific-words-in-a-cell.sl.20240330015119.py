# Start time: 2024-03-30 01:57:25.814503
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of times the second input (case-sensitive phrase) appears in the first input (expression), and given input as ['The fox jumped over the fox', 'fox'] output is 2, given input as ['The fox jumped over the fox', 'ox'] output is 2, given input as ['The fox jumped over the fox', 'Fox'] output is 0, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the number of times the second input (case-sensitive phrase) appears in the first input (expression)
# Input: ['The fox jumped over the fox', 'fox']
# Output: 2

def count_phrase_occurrences(expression, phrase):
    try:
        count = expression.count(phrase)
        return count
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(count_phrase_occurrences('The fox jumped over the fox', 'fox'))  # Output: 2
print(count_phrase_occurrences('The fox jumped over the fox', 'ox'))   # Output: 2
print(count_phrase_occurrences('The fox jumped over the fox', 'Fox'))  # Output: 0

# End time: 2024-03-30 01:57:29.897794
# Elapsed time in seconds: 4.083222097000544