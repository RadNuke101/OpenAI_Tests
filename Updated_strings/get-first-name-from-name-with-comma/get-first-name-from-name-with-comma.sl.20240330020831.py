# Start time: 2024-03-30 02:09:33.344307
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input is 1, return everything after the ",". else if the second input is 2, return everything before the ",", and given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if second input is 1, return everything after the ",", else if the second input is 2, return everything before the ","
# Input: ['Chang,Amy', '1'] Output: Amy
# Input: ['Chang,Amy', '2'] Output: Chang
# Input: ['smith,bobby', '2'] Output: smith
# Input: ['smith,bobby', '1'] Output: bobby

def process_input(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        input_str = input_list[0]
        option = int(input_list[1])
        
        if option == 1:
            output = input_str.split(',')[1].strip()
        elif option == 2:
            output = input_str.split(',')[0].strip()
        else:
            raise ValueError("Second input must be either 1 or 2")
        
        return output
    except (ValueError, IndexError) as e:
        return f"Error: {e}"

# Test cases
print(process_input(['Chang,Amy', '1']))  # Output: Amy
print(process_input(['Chang,Amy', '2']))  # Output: Chang
print(process_input(['smith,bobby', '2']))  # Output: smith
print(process_input(['smith,bobby', '1']))  # Output: bobby
print(process_input(['invalid_input']))  # Output: Error: Input list must contain exactly 2 elements
print(process_input(['Chang,Amy', '3']))  # Output: Error: Second input must be either 1 or 2

# End time: 2024-03-30 02:09:37.535924
# Elapsed time in seconds: 4.191523692001283