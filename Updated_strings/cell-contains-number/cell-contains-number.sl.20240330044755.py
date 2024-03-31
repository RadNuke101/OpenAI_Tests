# Start time: 2024-03-30 04:56:01.279235
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if a number is present in the inputted expression, return true, else false, and given input as ['A bird in the hand is worth 2 in the bush.'] output is true, given input as ['A bird in the hand is worth two in the bush.'] output is false, given input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if a number is present in the inputted expression, return true, else false
# Input: 'A bird in the hand is worth 2 in the bush.'
# Output: true

def check_for_number(input_str):
    try:
        for char in input_str:
            if char.isdigit():
                return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

# Test cases
print(check_for_number('A bird in the hand is worth 2 in the bush.'))  # Output: True
print(check_for_number('A bird in the hand is worth two in the bush.'))  # Output: False
print(check_for_number('The 15 shortcuts you simply must know'))  # Output: True

# End time: 2024-03-30 04:56:05.908194
# Elapsed time in seconds: 4.628947643999709