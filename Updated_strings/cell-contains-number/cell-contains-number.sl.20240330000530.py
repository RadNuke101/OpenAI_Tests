# Start time: 2024-03-30 00:13:56.125214
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if a number is present in the inputted expression, return true, else false, and given input as ['A bird in the hand is worth 2 in the bush.'] output is true, given input as ['A bird in the hand is worth two in the bush.'] output is false, given input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if a number is present in the inputted expression, return true, else false
# Input: 'A bird in the hand is worth 2 in the bush.' 
# Output: true

def check_for_number(input_str):
    try:
        words = input_str.split()
        for word in words:
            if any(char.isdigit() for char in word):
                return True
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False

# Test cases
print(check_for_number('A bird in the hand is worth 2 in the bush.'))  # Output: True
print(check_for_number('A bird in the hand is worth two in the bush.'))  # Output: False
print(check_for_number('The 15 shortcuts you simply must know'))  # Output: True

# End time: 2024-03-30 00:14:01.678841
# Elapsed time in seconds: 5.553597838000314