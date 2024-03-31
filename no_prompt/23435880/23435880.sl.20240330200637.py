# Start time: 2024-03-30 20:20:06.728406

# Content: Given that given input as ['apple apples', 'apple'] output is 2, given input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'apple apples', 'apple'
# Output: 2

# Input: 'an orange among the oranges is a spoiled orange', 'orange'
# Output: 3

def count_occurrences(sentence, word):
    try:
        count = sentence.count(word)
        return count
    except AttributeError:
        print("Error: Input must be strings.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(count_occurrences('apple apples', 'apple'))
print(count_occurrences('an orange among the oranges is a spoiled orange', 'orange'))

# End time: 2024-03-30 20:20:08.266957
# Elapsed time in seconds: 1.536841223999545