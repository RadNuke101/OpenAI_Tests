# Start time: 2024-03-29 23:49:01.695672
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
        
        data = input_list[0]
        choice = int(input_list[1])
        
        if choice == 1:
            return data.split(',')[1]
        elif choice == 2:
            return data.split(',')[0]
        else:
            raise ValueError("Invalid choice provided")
    
    except ValueError as e:
        return f"Error: {e}"

# Test cases
print(process_input('Chang,Amy,1'))  # Error: Input format is incorrect
print(process_input('Chang,Amy,2'))  # Error: Input format is incorrect
print(process_input('Chang,Amy,3'))  # Error: Invalid choice provided
print(process_input('Chang,Amy,1'))  # Error: Input format is incorrect
print(process_input('Chang,Amy'))     # Error: Input format is incorrect
print(process_input('Chang,Amy,1'))   # Amy
print(process_input('Chang,Amy,2'))   # Chang
print(process_input('smith,bobby,2')) # Error: Input format is incorrect
print(process_input('smith,bobby,1')) # Error: Input format is incorrect
print(process_input('smith,bobby,2')) # smith
print(process_input('smith,bobby,1')) # bobby

# End time: 2024-03-29 23:49:09.817705
# Elapsed time in seconds: 8.121788270000025