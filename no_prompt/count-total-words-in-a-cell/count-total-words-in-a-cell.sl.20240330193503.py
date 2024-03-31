# Start time: 2024-03-30 19:49:23.572532

# Content: Given that given input as ['humpty dumpty'] output is 2, given input as ['humpty dumpty sat on a wall,'] output is 6, given input as ['couldnt put humpty together again.'] output is 5, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'humpty dumpty', output: 2
# input: 'humpty dumpty sat on a wall,', output: 6
# input: 'couldnt put humpty together again.', output: 5

def count_words(input_str):
    try:
        words = input_str.split()
        return len(words)
    except AttributeError:
        print("Input is not a string")
    except:
        print("An error occurred")

# Test cases
print(count_words('humpty dumpty'))
print(count_words('humpty dumpty sat on a wall,'))
print(count_words('couldnt put humpty together again.'))

# End time: 2024-03-30 19:49:26.172117
# Elapsed time in seconds: 2.5995485769999505