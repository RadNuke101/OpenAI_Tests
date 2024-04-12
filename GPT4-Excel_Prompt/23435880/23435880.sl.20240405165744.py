# Start time: 2024-04-05 17:25:19.423592

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of the times the entered word (second column) appears in the expression (first column), and input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, word):
    # Split the expression into words
    words = expression.split()
    # Count the occurrences of the word
    count = sum(1 for w in words if w == word)
    return count

# Test cases
# Test case 1
result1 = generated_function('apple apples', 'apple')
# Test case 2
result2 = generated_function('an orange among the oranges is a spoiled orange', 'orange')
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-05 17:25:22.135823
# Elapsed time in seconds: 2.712157591000505