# Start time: 2024-04-10 15:40:19.559089

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The first input column contains phrases or sentences.
- The second input column contains specific words or phrases that are being searched for within the sentences.

Summary for Output Column Data:
- The output column contains boolean values (true or false) indicating whether the search term in the second input column was found in the corresponding sentence in the first input column.

Relationship between Input and Output:
- The output column reflects whether the search term provided in the second input column was present in the corresponding sentence from the first input column.
- If the output is true, it means that the search term was found in the sentence.
- If the output is false, it means that the search term was not found in the sentence., and input as ['An apple a day keeps the doctor away', 'apple'] output is true, input as ['An apple a day keeps the doctor away', 'orange'] output is false, input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str1, input_str2):
    # Split the input strings into sentences and search terms
    sentence = input_str1.split(',')[0].strip()
    search_term = input_str1.split(',')[1].strip()
    
    # Check if the search term is present in the sentence
    if search_term in sentence:
        return 'true'
    else:
        return 'false'

# Test cases
print(generated_function('An apple a day keeps the doctor away, apple'))
print(generated_function('An apple a day keeps the doctor away, orange'))
print(generated_function('Better the devil you know, you know'))
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true

# End time: 2024-04-10 15:40:21.714963
# Elapsed time in seconds: 2.155824849000055


# APPEND TEST SCRIPTS...
print(generated_function("An apple a day keeps the doctor away", "apple"))  ## Output: true
print(generated_function("An apple a day keeps the doctor away", "orange"))  ## Output: false
print(generated_function("Better the devil you know", "you know"))  ## Output: true


print(generated_function("A banana a day keeps the doctor away.", "orange"))  ### Output: [
print(generated_function("Better the devil you know", "devil"))  ### Output: f
print(generated_function("A banana a day keeps the doctor away.", "banana"))  ### Output: a
print(generated_function("A banana a day keeps the doctor away.", "doctor"))  ### Output: l

# TEST SCRIPTS APPENDED!

