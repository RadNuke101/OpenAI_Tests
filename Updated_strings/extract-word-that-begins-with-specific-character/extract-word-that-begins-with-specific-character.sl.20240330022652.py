# Start time: 2024-03-30 02:37:43.662299
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first phrase in the inputted epxression that begins with "_", and given input as ['this is a _username in the middle'] output is _username, given input as ['twitter names look like= _name'] output is _name, given input as ['with two _name1 and _name2'] output is _name1, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first phrase in the inputted expression that begins with "_"
# Input: 'this is a _username in the middle'
# Output: '_username'

def find_phrase_with_underscore(input_str):
    try:
        words = input_str.split()
        for word in words:
            if word.startswith('_'):
                return word
    except AttributeError:
        return "Invalid input, please enter a valid string."
    except Exception as e:
        return "An error occurred: " + str(e)

# Test cases
print(find_phrase_with_underscore('this is a _username in the middle'))  # Output: _username
print(find_phrase_with_underscore('twitter names look like= _name'))  # Output: _name
print(find_phrase_with_underscore('with two _name1 and _name2'))  # Output: _name1

# End time: 2024-03-30 02:37:46.973349
# Elapsed time in seconds: 3.310993717999736