# Start time: 2024-03-30 03:49:39.494894
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and given input as ['Ducati100'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Ducati250'] output is Ducati, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura100'] output is Acura, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def get_text_before_last_3_numbers(input_str):
    try:
        # Prompt: return the text before the last 3 numbers in inputted expression
        # Input: 'Ducati100', Output: 'Ducati'
        # Input: 'Honda125', Output: 'Honda'
        # Input: 'Ferrari250', Output: 'Ferrari'
        
        # Extract the text before the last 3 numbers
        text = ''.join([i for i in input_str if not i.isdigit() or i == ' '])
        return text.strip()
    
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(get_text_before_last_3_numbers('Ducati100'))  # Output: Ducati
print(get_text_before_last_3_numbers('Honda125'))  # Output: Honda
print(get_text_before_last_3_numbers('Ferrari250'))  # Output: Ferrari

# End time: 2024-03-30 03:49:47.340966
# Elapsed time in seconds: 7.845826840000882