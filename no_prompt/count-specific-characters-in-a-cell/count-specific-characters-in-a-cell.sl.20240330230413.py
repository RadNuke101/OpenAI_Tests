# Start time: 2024-03-30 23:16:03.105309

# Content: Given that given input as ['Hannah', 'n'] output is 2, given input as ['Hannah', 'x'] output is 0, given input as ['Hannah', 'N'] output is 0, given input as ['Hannah', 'a'] output is 2, given input as ['Hannah', 'h'] output is 1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'Hannah', 'n' => output: 2
# input: 'Hannah', 'x' => output: 0
# input: 'Hannah', 'N' => output: 0
# input: 'Hannah', 'a' => output: 2
# input: 'Hannah', 'h' => output: 1

def count_char_occurrences(input_str, char):
    try:
        count = input_str.lower().count(char.lower())
        return count
    except AttributeError:
        print("Error: Input must be a string")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(count_char_occurrences('Hannah', 'n'))
print(count_char_occurrences('Hannah', 'x'))
print(count_char_occurrences('Hannah', 'N'))
print(count_char_occurrences('Hannah', 'a'))
print(count_char_occurrences('Hannah', 'h'))

# End time: 2024-03-30 23:16:06.093675
# Elapsed time in seconds: 2.9882930769999803