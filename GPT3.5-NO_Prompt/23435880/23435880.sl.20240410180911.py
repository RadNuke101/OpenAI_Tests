# Start time: 2024-04-10 18:18:34.339806

'''
Prompt:
Given that input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string into the sentence and the word to search for
        input_list = input_str.split(', ')
        sentence = input_list[0]
        word = input_list[1]

        # Count the occurrences of the word in the sentence
        count = sentence.count(word)

        return count

    except Exception as e:
        return "Error: Invalid input format"

# Test cases
print(generated_function('apple apples, apple'))
print(generated_function('an orange among the oranges is a spoiled orange, orange'))
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-10 18:18:35.918014
# Elapsed time in seconds: 1.5781736580001962