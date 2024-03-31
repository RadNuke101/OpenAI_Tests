# Start time: 2024-03-30 02:01:09.124479
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the last phrase / word if all the letters are capitalized, and given input as ['Mining US'] output is Mining, given input as ['Soybean Farming CAN'] output is Soybean Farming, given input as ['Soybean Farming'] output is Soybean Farming, given input as ['Oil Extraction US'] output is Oil Extraction, given input as ['Fishing'] output is Fishing, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the last phrase / word if all the letters are capitalized
# Input: ['Mining US']
# Output: Mining

def process_input(input_str):
    try:
        input_str = input_str.strip()
        if input_str.isupper():
            return input_str.rsplit(' ', 1)[0]
        else:
            return input_str
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(process_input('Mining US'))  # Output: Mining
print(process_input('Soybean Farming CAN'))  # Output: Soybean Farming
print(process_input('Soybean Farming'))  # Output: Soybean Farming
print(process_input('Oil Extraction US'))  # Output: Oil Extraction
print(process_input('Fishing'))  # Output: Fishing

# End time: 2024-03-30 02:01:17.383185
# Elapsed time in seconds: 8.258555360000173