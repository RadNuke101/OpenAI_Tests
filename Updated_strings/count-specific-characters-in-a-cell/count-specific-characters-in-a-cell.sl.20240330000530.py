# Start time: 2024-03-30 00:17:07.506477
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of times the second input (case-sensitive letter) appears in the inputted expression (first input), and given input as ['Hannah', 'n'] output is 2, given input as ['Hannah', 'x'] output is 0, given input as ['Hannah', 'N'] output is 0, given input as ['Hannah', 'a'] output is 2, given input as ['Hannah', 'h'] output is 1, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the number of times the second input (case-sensitive letter) appears in the inputted expression (first input)
# Input: ['Hannah', 'n'] Output: 2
# Input: ['Hannah', 'x'] Output: 0
# Input: ['Hannah', 'N'] Output: 0
# Input: ['Hannah', 'a'] Output: 2
# Input: ['Hannah', 'h'] Output: 1

def count_letter_occurrences(expression, letter):
    try:
        count = expression.count(letter)
        return count
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(count_letter_occurrences('Hannah', 'n'))  # Output: 2
print(count_letter_occurrences('Hannah', 'x'))  # Output: 0
print(count_letter_occurrences('Hannah', 'N'))  # Output: 0
print(count_letter_occurrences('Hannah', 'a'))  # Output: 2
print(count_letter_occurrences('Hannah', 'h'))  # Output: 1

# End time: 2024-03-30 00:17:13.924018
# Elapsed time in seconds: 6.417505590000019