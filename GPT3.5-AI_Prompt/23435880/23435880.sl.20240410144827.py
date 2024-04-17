# Start time: 2024-04-10 15:06:04.594893

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
1. ['apple apples', 'apple']: The input column contains phrases related to apples. 
2. ['an orange among the oranges is a spoiled orange', 'orange']: The input column contains phrases related to oranges.

Output Column Summary:
- The output column contains the count of the target word mentioned in each input phrase.

Relationship Summary:
The input phrases in both columns contain references to specific fruits (apples and oranges), and the output column provides the count of occurrences of the target fruit word in each input phrase. The relationship between the input and output is that the output count corresponds to the number of times the target fruit word appears in the input phrase., and input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str, target_word):
    # Count the occurrences of the target word in the input string
    count = input_str.count(target_word)
    return count

# Test cases
print(generated_function('apple apples', 'apple'))  # Output: 2
print(generated_function('an orange among the oranges is a spoiled orange', 'orange'))  # Output: 3
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-10 15:06:06.127624
# Elapsed time in seconds: 1.5326954930001193