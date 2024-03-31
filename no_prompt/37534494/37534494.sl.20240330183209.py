# Start time: 2024-03-30 18:36:44.864085

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: "['I love apples', 'I hate bananas', 'banana']"
# Output: "I hate bananas"

def find_matching_sentence(input_str):
    try:
        input_list = input_str[1:-1].split(", ")
        keyword = input_str[-1]
        
        for sentence in input_list:
            if keyword in sentence:
                return sentence
        
        return "Keyword not found in any sentence"
    
    except Exception as e:
        return "Error: " + str(e)

# Test cases
print(find_matching_sentence("['I love apples', 'I hate bananas', 'banana']"))
print(find_matching_sentence("['I love apples', 'I hate bananas', 'apple']"))

# End time: 2024-03-30 18:36:46.910435
# Elapsed time in seconds: 2.0462920219999887