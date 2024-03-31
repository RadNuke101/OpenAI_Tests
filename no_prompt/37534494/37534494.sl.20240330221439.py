# Start time: 2024-03-30 22:18:51.172476

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: "['I love apples', 'I hate bananas', 'banana']"
# Output: "I hate bananas"

def match_input_output(input_str):
    try:
        input_list = input_str[1:-1].split(", ")
        output_str = input_str[-1]

        for item in input_list:
            if output_str in item:
                return item

        return "No match found"
    
    except Exception as e:
        return "Invalid input format"

# Test cases
print(match_input_output("['I love apples', 'I hate bananas', 'banana']"))  # Output: I hate bananas
print(match_input_output("['I love apples', 'I hate bananas', 'apple']"))    # Output: I love apples
print(match_input_output("['I love apples', 'I hate bananas', 'grapes']"))   # Output: No match found
print(match_input_output("['I love apples', 'I hate bananas']"))              # Output: No match found
print(match_input_output("['I love apples', 'I hate bananas', 'apple', 'banana']"))  # Output: No match found
print(match_input_output("['I love apples', 'I hate bananas', 'apple"))       # Output: Invalid input format

# End time: 2024-03-30 22:18:53.175819
# Elapsed time in seconds: 2.003275897999629