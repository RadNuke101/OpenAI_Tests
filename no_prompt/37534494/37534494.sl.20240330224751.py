# Start time: 2024-03-30 22:53:15.434567

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas

def find_matching_sentence(input_list, keyword):
    try:
        for sentence in input_list:
            if keyword in sentence:
                return sentence
        return "No matching sentence found"
    except Exception as e:
        return "Error: " + str(e)

# Test cases
input_list_1 = ['I love apples', 'I hate bananas', 'banana']
keyword_1 = 'banana'
print(find_matching_sentence(input_list_1, keyword_1))

input_list_2 = ['I love apples', 'I hate bananas', 'apple']
keyword_2 = 'apple'
print(find_matching_sentence(input_list_2, keyword_2))

# End time: 2024-03-30 22:53:16.710674
# Elapsed time in seconds: 1.2760826309986442