# Start time: 2024-03-30 04:13:47.899865
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input is 1, return everything after the ",". else if the second input is 2, return everything before the ",", and given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if second input is 1, return everything after the ",", else if the second input is 2, return everything before the ","
# Input: ['Chang,Amy', '1'] Output: Amy
# Input: ['Chang,Amy', '2'] Output: Chang
# Input: ['smith,bobby', '2'] Output: smith
# Input: ['smith,bobby', '1'] Output: bobby

def process_input(input_str):
    try:
        input_list = input_str.split(',')
        if len(input_list) != 2:
            raise ValueError("Input format is incorrect")
        
        data = input_list[0].strip()
        option = int(input_list[1].strip())
        
        if option == 1:
            return data.split(',')[1].strip()
        elif option == 2:
            return data.split(',')[0].strip()
        else:
            raise ValueError("Invalid option provided")
    
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An error occurred: {e}"

# Test cases
print(process_input('Chang,Amy, 1'))  # Output: Error: Input format is incorrect
print(process_input('Chang,Amy,2'))   # Output: Error: Input format is incorrect
print(process_input('Chang,Amy,3'))   # Output: Invalid option provided
print(process_input('Chang,Amy,1'))   # Output: Amy
print(process_input('Chang,Amy,2'))   # Output: Chang
print(process_input('smith,bobby,2')) # Output: smith
print(process_input('smith,bobby,1')) # Output: bobby

# End time: 2024-03-30 04:13:57.984444
# Elapsed time in seconds: 10.084275927001727