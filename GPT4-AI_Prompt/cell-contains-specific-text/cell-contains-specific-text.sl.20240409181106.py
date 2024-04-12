# Start time: 2024-04-09 18:38:59.508794

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains phrases or sentences, which are well-known English idioms or common sayings. These phrases are complete in themselves and convey a specific meaning or advice through their usage. Examples include "An apple a day keeps the doctor away" and "Better the devil you know." These sayings are part of the cultural lexicon and are often used to impart wisdom or advice in a concise manner.

The second column contains single words, which are intended to be checked for their presence within the phrases or sentences given in the first column. These words, such as "apple" and "orange," may or may not be directly related to the core message of the phrase but are rather focused on their literal occurrence within the given text.

### Output Column Summary:

The output data is binary, represented by boolean values true or false. These values indicate whether the word provided in the second input column is found within the phrase or sentence provided in the first input column. A true value signifies that the word is indeed present in the phrase, while a false value indicates the absence of the word. This output directly correlates with the presence or absence of specific words within the given phrases, making it a straightforward validation of inclusion.

### Relationship Summary:

The relationship between the input and output columns is based on the textual analysis of the phrases or sentences provided in the first input column against the words listed in the second input column. The process involves examining whether the given word is a part of the phrase or sentence. If the word is found within the text, the relationship yields a true outcome, indicating a match. Conversely, if the word is not found within the text, the relationship results in a false outcome, indicating no match.

This relationship showcases a simple yet effective method of textual analysis focused on word presence, which can be utilized in various applications such as keyword searching, content filtering, or even educational tools to help with language learning. The binary nature of the output simplifies the interpretation of results, making it accessible for users to understand whether a specific word is included in a given phrase or not., and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase, word):
    # Check if the word is present in the phrase
    return word in phrase

# Test cases based on the provided examples
# Test case 1: Checking if 'apple' is in 'An apple a day keeps the doctor away'
print(generated_function('An apple a day keeps the doctor away', 'apple'))  # Expected output: True

# Test case 2: Checking if 'orange' is in 'An apple a day keeps the doctor away'
print(generated_function('An apple a day keeps the doctor away', 'orange'))  # Expected output: False

# Test case 3: Checking if 'you know' is in 'Better the devil you know'
print(generated_function('Better the devil you know', 'you know'))  # Expected output: True
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-09 18:39:08.113319
# Elapsed time in seconds: 8.604484519000835