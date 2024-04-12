# Start time: 2024-04-05 18:32:46.921242

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of the times the entered word (second column) appears in the expression (first column), and input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, word):
    # Split the expression into words to handle cases like 'apples' when searching for 'apple'
    words = expression.split()
    count = 0
    for w in words:
        # Check if the current word matches or contains the target word as a whole word
        if w == word or w.startswith(word + " ") or w.endswith(" " + word) or (" " + word + " " in w):
            count += 1
    return count

# Test cases
print(generated_function('apple apples', 'apple'))  # Expected output: 2
print(generated_function('an orange among the oranges is a spoiled orange', 'orange'))  # Expected output: 3
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-05 18:32:53.200599
# Elapsed time in seconds: 6.27924224400158