# Start time: 2024-04-09 12:54:05.141263

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains phrases or sentences, which are well-known English proverbs or idiomatic expressions. These expressions are complete thoughts, often used to convey wisdom or advice in a concise manner. Examples from the provided data include "An apple a day keeps the doctor away" and "Better the devil you know."

The second column contains single words, which are intended to be searched for within the phrases or sentences of the first column. These words are either directly extracted from the sentences in the first column or are unrelated words. The examples given include "apple," which is present in the first sentence, and "orange," which is not found in any of the provided sentences.

### Output Column Summary:

The output data is a series of boolean values (true or false), each corresponding to a pair of inputs from the two input columns. The output value is true if the word from the second input column is found within the phrase or sentence from the first input column. Conversely, the output is false if the word is not found within the phrase or sentence. This binary output directly reflects the presence or absence of the specified word within the given phrase or sentence.

### Relationship Summary:

The relationship between the input and the output columns is a direct function of word presence. The output (true or false) is determined by whether the word specified in the second input column is contained within the phrase or sentence provided in the first input column. This relationship showcases a basic text search operation, where the task is to identify whether a substring (the word) is part of a larger string (the phrase or sentence). The process is akin to a simple search or match function, which is fundamental in text processing and analysis tasks. The nature of the data and the relationship between the inputs and outputs suggest a straightforward, rule-based logical operation, highlighting the basics of string matching in data processing and natural language processing contexts., and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase, word):
    """
    This function checks if a given word is present in a phrase.
    
    Parameters:
    - phrase (str): The phrase or sentence to search within.
    - word (str): The word to search for in the phrase.
    
    Returns:
    - bool: True if the word is found in the phrase, False otherwise.
    """
    return word in phrase

# Test cases
# Test case 1: Word is present in the phrase
result1 = generated_function('An apple a day keeps the doctor away', 'apple')
# Expected output: True

# Test case 2: Word is not present in the phrase
result2 = generated_function('An apple a day keeps the doctor away', 'orange')
# Expected output: False

# Test case 3: Phrase contains the sequence of words being searched
result3 = generated_function('Better the devil you know', 'you know')
# Expected output: True
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-09 12:54:14.331298
# Elapsed time in seconds: 9.18985385499991