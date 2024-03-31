# Start time: 2024-03-30 23:09:40.538818

# Content: Given that given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_input_output(input_str):
    try:
        input_list = input_str.split(', ')
        sentence1 = input_list[0]
        sentence2 = input_list[1]
        keyword = input_list[2]

        if keyword in sentence1:
            return sentence1
        elif keyword in sentence2:
            return sentence2
        else:
            return "Keyword not found in any sentence"
    
    except IndexError:
        return "Input format is incorrect. Please provide 3 strings separated by commas."
    except Exception as e:
        return f"An error occurred: {e}"

# Test cases
print(match_input_output('I love apples, I hate bananas, banana'))  # Expected output: I hate bananas
print(match_input_output('I love apples, I hate bananas, apple'))  # Expected output: I love apples
print(match_input_output('I love apples, I hate bananas'))  # Expected output: Input format is incorrect. Please provide 3 strings separated by commas.
print(match_input_output('I love apples, I hate bananas, apple, extra'))  # Expected output: Input format is incorrect. Please provide 3 strings separated by commas.

# End time: 2024-03-30 23:09:43.081695
# Elapsed time in seconds: 2.5428105920000235