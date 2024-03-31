# Start time: 2024-03-29 23:41:07.048788
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
# Input: 'Ferrari250', Output: 'Ferrari'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'

def extract_text(input_str):
    try:
        # Check if the input is a string
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
        
        # Find the index of the last occurrence of a number in the input string
        last_num_index = max([input_str.rfind(str(i)) for i in range(10)])
        
        # Find the index of the text before the last 3 numbers
        text_index = max([input_str.rfind(str(i)) for i in range(last_num_index - 2)])
        
        # Extract the text before the last 3 numbers
        extracted_text = input_str[:text_index]
        
        return extracted_text
    except Exception as e:
        return str(e)

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
print(extract_text('Ferrari250')) # Output: Ferrari
print(extract_text('Honda550'))   # Output: Honda
print(extract_text('Ducati125'))  # Output: Ducati

# End time: 2024-03-29 23:41:17.633839
# Elapsed time in seconds: 10.583023099999991