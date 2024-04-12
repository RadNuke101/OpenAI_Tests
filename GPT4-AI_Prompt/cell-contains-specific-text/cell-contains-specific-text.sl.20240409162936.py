# Start time: 2024-04-09 16:57:32.850472

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns. The first column contains phrases or sentences, which are well-known English idioms or common expressions. These expressions are complete thoughts and are used to convey specific ideas, wisdom, or advice in a metaphorical or literal sense. Examples include "An apple a day keeps the doctor away" and "Better the devil you know." These phrases are culturally significant and often used in everyday language to express a wide range of emotions, advice, or general truths.

The second column contains single words, which are intended to be searched for within the phrases or sentences provided in the first column. These words are significant in the context of the phrases, either being key components of the idioms themselves or completely unrelated words. Examples include "apple" and "orange."

### Output Column Summary:

The output data is a series of boolean values (true or false), which represent whether the word provided in the second input column is found within the phrase or sentence provided in the first input column. A value of true indicates that the word is present in the phrase, while a value of false indicates that the word is not found within the phrase. This output reflects a straightforward relationship between the presence of a specific word within a given phrase and the binary outcome.

### Relationship Summary:

The relationship between the input and the output columns is a direct mapping of the presence or absence of a specific word (from the second input column) within a given phrase or sentence (from the first input column). When the word is found within the phrase, the output is true, indicating a successful match. Conversely, when the word is not found within the phrase, the output is false, indicating no match. This relationship showcases a simple text search or word matching process, where the task is to verify if a given word is part of a larger string of text. The process is binary and deterministic, relying solely on the occurrence of the word within the phrase to determine the outcome., and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
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
    # Check if the word is in the phrase
    return word in phrase

# Test cases
print(generated_function('An apple a day keeps the doctor away', 'apple'))  # Expected output: True
print(generated_function('An apple a day keeps the doctor away', 'orange'))  # Expected output: False
print(generated_function('Better the devil you know', 'you know'))  # Expected output: True
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-09 16:57:39.900794
# Elapsed time in seconds: 7.050221284000145