# Start time: 2024-03-30 00:28:06.732006
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the second input (word or phrase) is in the first input (expression), return true, else false, and given input as ['An apple a day keeps the doctor away', 'apple'] output is true, given input as ['An apple a day keeps the doctor away', 'orange'] output is false, given input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the second input (word or phrase) is in the first input (expression), return true, else false
# Input: 'An apple a day keeps the doctor away', 'apple'
# Output: true
# Input: 'An apple a day keeps the doctor away', 'orange'
# Output: false
# Input: 'Better the devil you know', 'you know'
# Output: true

def check_input(input_str, check_str):
    try:
        if check_str in input_str:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(check_input('An apple a day keeps the doctor away', 'apple'))  # Output: True
print(check_input('An apple a day keeps the doctor away', 'orange'))  # Output: False
print(check_input('Better the devil you know', 'you know'))  # Output: True

# End time: 2024-03-30 00:28:11.925640
# Elapsed time in seconds: 5.193582246999995