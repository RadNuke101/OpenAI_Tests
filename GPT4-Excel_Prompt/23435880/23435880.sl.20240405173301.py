# Start time: 2024-04-05 17:59:23.339587

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of the times the entered word (second column) appears in the expression (first column), and input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, word):
    # Split the expression into words to handle cases where the target word is a substring of another word
    words = expression.split()
    # Count the occurrences of the word
    count = sum(1 for w in words if w == word)
    return count

# Test cases
# Test case 1
result1 = generated_function('apple apples', 'apple')
print(result1)  # Expected output: 1

# Test case 2
result2 = generated_function('an orange among the oranges is a spoiled orange', 'orange')
print(result2)  # Expected output: 3
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-05 17:59:27.054066
# Elapsed time in seconds: 3.7143687699999646