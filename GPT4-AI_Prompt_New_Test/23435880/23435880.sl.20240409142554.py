# Start time: 2024-04-09 16:01:29.285449

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of two columns, each containing text strings. The first column includes sentences or phrases that contain one or more instances of a specific word, which is the focus of the analysis. These instances can vary in their form, appearing in both singular and plural forms or as part of different words. The second column specifies the target word for which the occurrences are to be counted within the corresponding sentence or phrase in the first column. The target word is presented in its singular or base form.

### Output Column Summary:

The output data is a single column that provides numerical values. Each value corresponds to the count of occurrences of the target word (specified in the second input column) within the sentence or phrase provided in the first input column. The count includes all forms of the target word, whether singular, plural, or as part of another word, as long as the base form of the target word is identifiable within the counted word.

### Relationship Summary:

The relationship between the input and output columns is a function of text analysis focused on word occurrence counting. For each row, the process involves identifying the target word specified in the second input column and counting how many times this target word, in any of its applicable forms, appears within the sentence or phrase provided in the first input column. The output value is directly proportional to the frequency of the target word's occurrence within the text. This relationship demonstrates a basic form of text analysis, where the input data (text and target word) directly determines the output data (count of target word occurrences). The process highlights the importance of understanding both the context and the variations of word usage within natural language to accurately count and represent the occurrences of specific words., and input as ['apple apples', 'apple'] output is 2, input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

import re

def generated_function(sentence, target_word):
    """
    Counts the occurrences of the target word in its various forms within the given sentence.
    
    :param sentence: A string containing the sentence or phrase to be analyzed.
    :param target_word: The base form of the target word to count within the sentence.
    :return: The count of occurrences of the target word in its various forms.
    """
    # Create a pattern to match the target word in its various forms
    pattern = r'\b' + re.escape(target_word) + r'\b|\b' + re.escape(target_word) + r's\b'
    
    # Find all matches of the pattern in the sentence
    matches = re.findall(pattern, sentence, re.IGNORECASE)
    
    # Return the count of matches
    return len(matches)

# Test cases
print(generated_function('apple apples', 'apple'))  # Expected output: 2
print(generated_function('an orange among the oranges is a spoiled orange', 'orange'))  # Expected output: 3
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3

# End time: 2024-04-09 16:01:37.840080
# Elapsed time in seconds: 8.554409917000157


# APPEND TEST SCRIPTS...
print(generated_function("apple apples", "apple"))  ## Output: 2
print(generated_function("an orange among the oranges is a spoiled orange", "orange"))  ## Output: 3


print(generated_function("banana bananas", "banana"))  ### Output: 2
print(generated_function("a banana bananas", "banana"))  ### Output: 2
print(generated_function("a bananas banana", "banana"))  ### Output: 2
print(generated_function("an lemon among the lemons is a spoiled", "lemon"))  ### Output: 2
print(generated_function("an lemon among the lemons is a spoiled lemon", "lemon"))  ### Output: 3

# TEST SCRIPTS APPENDED!

