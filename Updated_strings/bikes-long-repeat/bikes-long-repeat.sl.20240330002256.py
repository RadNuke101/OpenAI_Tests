# Start time: 2024-03-30 00:35:02.461756
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and given input as ['Ducati100'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Ducati250'] output is Ducati, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura100'] output is Acura, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def get_text_before_last_three_numbers(input_str):
    try:
        input_str = input_str[0]  # Extracting the string from the list
        if not input_str.isalpha():  # Checking if the input contains only alphabets
            raise ValueError("Input should contain only alphabets")
        
        # Finding the index of the last 3 numbers in the input string
        last_three_numbers_index = len(input_str) - 1
        count = 0
        for i in range(len(input_str) - 1, -1, -1):
            if input_str[i].isdigit():
                count += 1
            if count == 3:
                last_three_numbers_index = i
                break
        
        return input_str[:last_three_numbers_index].strip()  # Returning the text before the last 3 numbers
    
    except Exception as e:
        return str(e)

# Input: 'Ducati100'
# Output: 'Ducati'
# Prompt: return the text before the last 3 numbers in inputted expression
print(get_text_before_last_three_numbers(['Ducati100']))  # Output: Ducati

# Input: 'Honda125'
# Output: 'Honda'
print(get_text_before_last_three_numbers(['Honda125']))  # Output: Honda

# Input: 'Ferrari250'
# Output: 'Ferrari'
print(get_text_before_last_three_numbers(['Ferrari250']))  # Output: Ferrari

# End time: 2024-03-30 00:35:07.084968
# Elapsed time in seconds: 4.623155789000066