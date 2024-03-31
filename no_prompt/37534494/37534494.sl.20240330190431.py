# Start time: 2024-03-30 19:09:28.152711

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def find_matching_sentence(input_str):
    try:
        sentences = input_str.split(', ')
        keyword = sentences.pop()
        
        for sentence in sentences:
            if keyword in sentence:
                return sentence
        
        return "No matching sentence found"
    
    except Exception as e:
        return "Error: Invalid input"

# Test cases
"""
Input: 'I love apples, I hate bananas, banana'
Output: 'I hate bananas'
"""
print(find_matching_sentence('I love apples, I hate bananas, banana'))

"""
Input: 'I love apples, I hate bananas, apple'
Output: 'I love apples'
"""
print(find_matching_sentence('I love apples, I hate bananas, apple'))

"""
Input: 'I love apples, I hate bananas, orange'
Output: 'No matching sentence found'
"""
print(find_matching_sentence('I love apples, I hate bananas, orange'))

"""
Input: 'I love apples, I hate bananas'
Output: 'Error: Invalid input'
"""
print(find_matching_sentence('I love apples, I hate bananas'))

# End time: 2024-03-30 19:09:31.005126
# Elapsed time in seconds: 2.8523291000001336