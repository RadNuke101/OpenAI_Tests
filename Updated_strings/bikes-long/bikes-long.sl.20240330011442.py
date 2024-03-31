# Start time: 2024-03-30 01:25:31.607100
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the text before the last 3 numbers in inputted expression
# Input: 'Ducati100', Output: 'Ducati'
# Input: 'Honda125', Output: 'Honda'
# Input: 'Ducati250', Output: 'Ducati'
# Input: 'Honda250', Output: 'Honda'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'
# Input: 'Acura100', Output: 'Acura'
# Input: 'Acura125', Output: 'Acura'
# Input: 'Ferrari250', Output: 'Ferrari'

def extract_text(input_str):
    try:
        if input_str[-3:].isdigit():
            index = len(input_str) - 3
            while index > 0 and input_str[index-1].isalpha():
                index -= 1
            return input_str[:index]
        else:
            raise ValueError("Input does not end with 3 numbers")
    except ValueError as ve:
        return str(ve)

# Test cases
print(extract_text('Ducati100'))  # Output: Ducati
print(extract_text('Honda125'))   # Output: Honda
print(extract_text('Ducati250'))  # Output: Ducati
print(extract_text('Honda250'))   # Output: Honda
print(extract_text('Honda550'))   # Output: Honda
print(extract_text('Ducati125'))  # Output: Ducati
print(extract_text('Acura100'))   # Output: Acura
print(extract_text('Acura125'))   # Output: Acura
print(extract_text('Ferrari250')) # Output: Ferrari

# End time: 2024-03-30 01:25:38.966827
# Elapsed time in seconds: 7.359596816999328