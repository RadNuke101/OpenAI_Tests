# Start time: 2024-03-30 04:43:43.571987
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of the times the entered word (second column) appears in the expression (first column), and given input as ['apple apples', 'apple'] output is 2, given input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the number of the times the entered word (second column) appears in the expression (first column)
# Input: ['apple apples', 'apple'] Output: 2
# Input: ['an orange among the oranges is a spoiled orange', 'orange'] Output: 3

def count_word_appearance(expression, word):
    try:
        count = expression.count(word)
        return count
    except Exception as e:
        return "Error: " + str(e)

# Test the function with the provided inputs
print(count_word_appearance('apple apples', 'apple'))  # Output: 2
print(count_word_appearance('an orange among the oranges is a spoiled orange', 'orange'))  # Output: 3

# End time: 2024-03-30 04:43:47.703280
# Elapsed time in seconds: 4.131277378000959