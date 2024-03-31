# Start time: 2024-03-30 20:10:56.590136

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def find_matching_sentence(sentences, keyword):
    try:
        for sentence in sentences:
            if keyword in sentence:
                return sentence
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas
print(find_matching_sentence(['I love apples', 'I hate bananas', 'banana'], 'banana'))

# Input: ['I love apples', 'I hate bananas', 'apple']
# Output: I love apples
print(find_matching_sentence(['I love apples', 'I hate bananas', 'apple'], 'apple'))

# End time: 2024-03-30 20:10:58.704160
# Elapsed time in seconds: 2.1139990800002124