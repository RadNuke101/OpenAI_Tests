# Start time: 2024-03-30 03:49:27.549340
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the input followed by a space, and if there is a 1 in the input return "apple", if there is a 2 in the input return "bananas", if there is a 3 in the input return "strawberries", if there is a 4 in the input return "oranges", and given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first word of the input followed by a space, and if there is a 1 in the input return "apple",
# if there is a 2 in the input return "bananas", if there is a 3 in the input return "strawberries",
# if there is a 4 in the input return "oranges"

def process_input(input_str):
    try:
        input_word, input_num = input_str.split(', ')
        output = input_word + ' '
        
        if '1' in input_num:
            output += 'apple'
        elif '2' in input_num:
            output += 'bananas'
        elif '3' in input_num:
            output += 'strawberries'
        elif '4' in input_num:
            output += 'oranges'
        
        return output
    except Exception as e:
        return "Invalid input"

# Test cases
print(process_input('one, 1'))  # Output: one apple
print(process_input('two, 2'))  # Output: two bananas
print(process_input('three, 3'))  # Output: three strawberries
print(process_input('four, 4'))  # Output: four oranges
print(process_input('invalid input'))  # Output: Invalid input

# End time: 2024-03-30 03:49:32.187201
# Elapsed time in seconds: 4.637718540001515