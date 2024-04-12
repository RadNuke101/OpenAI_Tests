# Start time: 2024-04-05 16:15:01.326855

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of the times the entered word (second column) appears in the expression (first column), and input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, word):
    # Split the expression into words to handle cases where words are part of other words
    words = expression.split()
    # Count the occurrences of the word in the list of words
    count = sum(1 for w in words if w == word)
    return count

# Test cases
# Test case 1: 'apple apples', 'apple' should return 2
result1 = generated_function('apple apples', 'apple')
# Test case 2: 'an orange among the oranges is a spoiled orange', 'orange' should return 3
result2 = generated_function('an orange among the oranges is a spoiled orange', 'orange')
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-05 16:15:06.260203
# Elapsed time in seconds: 4.933208248000028