# Start time: 2024-04-10 15:10:11.889602

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Data Summaries:
1. The first input column contains sentences with placeholders for usernames.
2. The second input column specifies the username to be searched for in the sentences.

Output Column Data Summary:
1. The output column contains the count of occurrences of the specified username in each sentence.

Relationship Summary:
The input column data consists of sentences with placeholders for usernames, and the output column data provides the count of occurrences of the specified username in each sentence. The relationship between the input and output is that the output column quantifies the number of times the specified username appears in each sentence from the input column data. This relationship allows for easy identification of the frequency of the specified username within the provided sentences., and input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'] output is 2, input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'] output is 1, input as ['An _example string with _example in it is awesome _example', 'example'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str, username):
    # Split the input string into sentences
    sentences = input_str.split(', ')
    
    # Initialize a variable to store the count of occurrences
    count = 0
    
    # Iterate through each sentence
    for sentence in sentences:
        # Count the occurrences of the specified username in the sentence
        count += sentence.count(username)
    
    return count

# Test cases
print(generated_function('An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'))
print(generated_function('An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'))
print(generated_function('An _example string with _example in it is awesome _example', 'example'))
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "username"))  ## Output: 2
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "AwesomeUser"))  ## Output: 1
print(generated_function("An _example string with _example in it is awesome _example", "example"))  ## Output: 3

# End time: 2024-04-10 15:10:14.667700
# Elapsed time in seconds: 2.7780381439997655