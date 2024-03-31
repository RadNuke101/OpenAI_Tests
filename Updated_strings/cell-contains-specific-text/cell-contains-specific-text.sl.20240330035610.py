# Start time: 2024-03-30 04:00:54.736554
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word or phrase) is in the first input (expression), return true, else false, and given input as ['An apple a day keeps the doctor away', 'apple'] output is true, given input as ['An apple a day keeps the doctor away', 'orange'] output is false, given input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the second input (word or phrase) is in the first input (expression), return true, else false
# Input: 'An apple a day keeps the doctor away', 'apple'
# Output: True

def check_input(expression, word):
    try:
        if word in expression:
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(check_input('An apple a day keeps the doctor away', 'apple'))  # True
print(check_input('An apple a day keeps the doctor away', 'orange'))  # False
print(check_input('Better the devil you know', 'you know'))  # True

# End time: 2024-03-30 04:00:56.542085
# Elapsed time in seconds: 1.8054811710007925