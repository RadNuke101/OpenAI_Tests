# Start time: 2024-04-05 16:20:53.041275

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return count of the phrase (second column) in expression (first column), and input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'] output is 2, input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'] output is 1, input as ['An _example string with _example in it is awesome _example', 'example'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, phrase):
    # Splitting the expression by spaces to handle cases where the phrase is part of a larger word
    words = expression.split()
    # Counting occurrences where the phrase exactly matches or is part of a larger word with underscores
    count = sum(1 for word in words if phrase in word.strip("_"))
    return count

# Test cases
generated_function('An example string with _username in it RT _AwesomeUser says _username is awesome', 'username')
generated_function('An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser')
generated_function('An _example string with _example in it is awesome _example', 'example')
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "username"))  ## Output: 2
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "AwesomeUser"))  ## Output: 1
print(generated_function("An _example string with _example in it is awesome _example", "example"))  ## Output: 3

# End time: 2024-04-05 16:20:57.292640
# Elapsed time in seconds: 4.251242421999905