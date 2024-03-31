# Start time: 2024-03-30 00:59:25.920685
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if both the first and second inputs match exactly, including capitalization, return true, else false, and given input as ['apple', 'apple'] output is true, given input as ['orange', 'Orange'] output is false, given input as ['peach', 'peach'] output is true, given input as ['cherry', 'cherrY'] output is false, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if both the first and second inputs match exactly, including capitalization, return true, else false
# Input: ['apple', 'apple'] Output: true
# Input: ['orange', 'Orange'] Output: false
# Input: ['peach', 'peach'] Output: true
# Input: ['cherry', 'cherrY'] Output: false

def compare_strings(input1, input2):
    try:
        if input1 == input2:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(compare_strings('apple', 'apple'))  # Output: True
print(compare_strings('orange', 'Orange'))  # Output: False
print(compare_strings('peach', 'peach'))  # Output: True
print(compare_strings('cherry', 'cherrY'))  # Output: False

# End time: 2024-03-30 00:59:32.169057
# Elapsed time in seconds: 6.248195211000166