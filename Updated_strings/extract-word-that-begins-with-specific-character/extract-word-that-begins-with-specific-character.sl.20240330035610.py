# Start time: 2024-03-30 04:05:18.691945
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first phrase in the inputted epxression that begins with "_", and given input as ['this is a _username in the middle'] output is _username, given input as ['twitter names look like= _name'] output is _name, given input as ['with two _name1 and _name2'] output is _name1, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first phrase in the inputted expression that begins with "_"
# Input: 'this is a _username in the middle'
# Output: '_username'

def find_phrase_with_underscore(input_str):
    try:
        # Split the input string into words
        words = input_str.split()
        
        # Find the first word that starts with "_"
        for word in words:
            if word.startswith("_"):
                return word
        
        return None  # Return None if no phrase with "_" is found
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(find_phrase_with_underscore('this is a _username in the middle'))  # Output: '_username'
print(find_phrase_with_underscore('twitter names look like= _name'))  # Output: '_name'
print(find_phrase_with_underscore('with two _name1 and _name2'))  # Output: '_name1'

# End time: 2024-03-30 04:05:22.287855
# Elapsed time in seconds: 3.5958296040007554