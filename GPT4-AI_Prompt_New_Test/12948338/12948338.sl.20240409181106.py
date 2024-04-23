# Start time: 2024-04-09 19:50:40.104984

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two primary components per row: a string of text and a target word. The text strings are composed of sentences that include various words, among which are usernames prefixed with an underscore (_). These usernames appear to be a significant focus within the strings. The target word provided alongside each string is a keyword that the analysis seeks to find within the context of the text, specifically looking at its occurrences in a particular format (e.g., as part of a username).

1. **Text Strings**: These are sentences that contain a mix of regular words, special characters (like underscores), and usernames. The usernames are highlighted by being prefixed with an underscore. The sentences simulate scenarios where a username is mentioned in different contexts, possibly reflecting social media posts or comments.

2. **Target Words**: Each row includes a target word that seems to be the focus of the analysis. The task appears to involve identifying occurrences of this target word within the text, particularly when it is part of a username (denoted by an underscore prefix).

### Output Column Summary:

The output data is numerical, representing the count of occurrences of the target word within the text strings, specifically when it appears as part of a username (underscore-prefixed). The numbers vary based on how frequently the target word, in its specified format, is found within each text string.

### Relationship Summary:

The relationship between the input and output columns is a function of text analysis focused on identifying specific patterns within sentences. The task involves counting how many times a target word appears as part of a username within the provided text strings. The usernames are uniquely identified by an underscore prefix, and the analysis is case-sensitive, given the examples provided.

- The first component of the input (text string) provides the context and content for analysis, containing potential instances of the target word.
- The second component (target word) specifies what to look for within the text, guiding the search process.
- The output quantifies the result of this search, offering a count of how many times the target word was found in the specified format (as part of a username).

This relationship showcases a straightforward text analysis task where the input data's structure and content directly influence the numerical output, reflecting the frequency of specified patterns (underscore-prefixed target words) within the text., and input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'] output is 2, input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'] output is 1, input as ['An _example string with _example in it is awesome _example', 'example'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(text_string, target_word):
    # Split the text string into individual words to analyze each separately
    words = text_string.split()
    # Initialize a counter to keep track of occurrences
    count = 0
    # Iterate through each word in the split text
    for word in words:
        # Check if the word starts with an underscore and contains the target word
        if word.startswith('_') and target_word in word[1:]:
            # Increment the count if the condition is met
            count += 1
    # Return the total count of occurrences
    return count

# Test cases
print(generated_function('An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'))  # Expected output: 2
print(generated_function('An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'))  # Expected output: 1
print(generated_function('An _example string with _example in it is awesome _example', 'example'))  # Expected output: 3
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "username"))  ## Output: 2
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "AwesomeUser"))  ## Output: 1
print(generated_function("An _example string with _example in it is awesome _example", "example"))  ## Output: 3

# End time: 2024-04-09 19:50:49.634270
# Elapsed time in seconds: 9.529108072998497


# APPEND TEST SCRIPTS...
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "username"))  ## Output: 2
print(generated_function("An example string with _username in it RT _AwesomeUser says _username is awesome", "AwesomeUser"))  ## Output: 1
print(generated_function("An _example string with _example in it is awesome _example", "example"))  ## Output: 3


print(generated_function("An _example string with _example is awesome _example", "example"))  ### Output: 3
print(generated_function("An example string with _username RT _AwesomeUser says _username is awesome", "AwesomeUser"))  ### Output: 1
print(generated_function("An example string with _username RT _AwesomeUser says _username is awesome", "username"))  ### Output: 2
print(generated_function("An _example _string with _example is awesome _example", "string"))  ### Output: 1

# TEST SCRIPTS APPENDED!

