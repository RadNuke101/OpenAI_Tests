# Start time: 2024-03-30 01:02:24.216667
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column), and given input as ['I love apples', 'I hate bananas', 'banana'] output is I hate bananas, given input as ['I love apples', 'I hate bananas', 'apple'] output is I love apples, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: given two phrases as the first two inputs, return the phrase (first or second column) which contains the third inputted word (third column)
# Input: ['I love apples', 'I hate bananas', 'banana']
# Output: I hate bananas
# Input: ['I love apples', 'I hate bananas', 'apple']
# Output: I love apples

def find_matching_phrase(input1, input2, word):
    try:
        if word in input1:
            return input1
        elif word in input2:
            return input2
        else:
            return "No matching phrase found"
    except Exception as e:
        return str(e)

# Test cases
print(find_matching_phrase('I love apples', 'I hate bananas', 'banana'))  # Output: I hate bananas
print(find_matching_phrase('I love apples', 'I hate bananas', 'apple'))   # Output: I love apples

# End time: 2024-03-30 01:02:30.267474
# Elapsed time in seconds: 6.05063934699956