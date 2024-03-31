# Start time: 2024-03-29 23:38:53.993994
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if a number is present in the inputted expression, return true, else false, and given input as ['A bird in the hand is worth 2 in the bush.'] output is true, given input as ['A bird in the hand is worth two in the bush.'] output is false, given input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if a number is present in the inputted expression, return true, else false
# Input: 'A bird in the hand is worth 2 in the bush.'
# Output: true

# Input: 'A bird in the hand is worth two in the bush.'
# Output: false

# Input: 'The 15 shortcuts you simply must know'
# Output: true

def check_number_presence(input_str):
    try:
        for char in input_str:
            if char.isdigit():
                return True
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False

# Test cases
print(check_number_presence('A bird in the hand is worth 2 in the bush.'))  # Output: true
print(check_number_presence('A bird in the hand is worth two in the bush.'))  # Output: false
print(check_number_presence('The 15 shortcuts you simply must know'))  # Output: true

# End time: 2024-03-29 23:38:56.377880
# Elapsed time in seconds: 2.3838147430000163