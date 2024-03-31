# Start time: 2024-03-30 04:57:51.850014
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the last phrase / word if all the letters are capitalized, and given input as ['Mining US'] output is Mining, given input as ['Soybean Farming CAN'] output is Soybean Farming, given input as ['Soybean Farming'] output is Soybean Farming, given input as ['Oil Extraction US'] output is Oil Extraction, given input as ['Fishing'] output is Fishing, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the last phrase / word if all the letters are capitalized
# Input: ['Mining US'] 
# Output: Mining
# Input: ['Soybean Farming CAN'] 
# Output: Soybean Farming
# Input: ['Soybean Farming'] 
# Output: Soybean Farming
# Input: ['Oil Extraction US'] 
# Output: Oil Extraction
# Input: ['Fishing'] 
# Output: Fishing

def process_input(input_str):
    try:
        input_str = input_str.strip()
        words = input_str.split()
        
        if len(words) == 1:
            return input_str
        
        last_word = words[-1]
        if last_word.isupper():
            return ' '.join(words[:-1])
        else:
            return input_str
    except Exception as e:
        return "Error processing input: " + str(e)

# Test cases
print(process_input('Mining US'))  # Output: Mining
print(process_input('Soybean Farming CAN'))  # Output: Soybean Farming
print(process_input('Soybean Farming'))  # Output: Soybean Farming
print(process_input('Oil Extraction US'))  # Output: Oil Extraction
print(process_input('Fishing'))  # Output: Fishing

# End time: 2024-03-30 04:57:54.578236
# Elapsed time in seconds: 2.7282910450012423