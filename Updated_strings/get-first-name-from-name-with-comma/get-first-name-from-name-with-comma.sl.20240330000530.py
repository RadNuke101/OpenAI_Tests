# Start time: 2024-03-30 00:06:22.091387
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input is 1, return everything after the ",". else if the second input is 2, return everything before the ",", and given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if second input is 1, return everything after the ",". 
# else if the second input is 2, return everything before the ","
# Input: ['Chang,Amy', '1'] Output: Amy
# Input: ['Chang,Amy', '2'] Output: Chang
# Input: ['smith,bobby', '2'] Output: smith
# Input: ['smith,bobby', '1'] Output: bobby

def process_input(input_str):
    try:
        input_list = input_str.split(',')
        if len(input_list) != 2:
            raise ValueError("Invalid input format. Please provide input in the format 'string,string'.")
        
        data = input_list[0]
        option = int(input_list[1])
        
        if option == 1:
            return data.split(',')[1]
        elif option == 2:
            return data.split(',')[0]
        else:
            raise ValueError("Invalid option. Please provide 1 or 2 as the second input.")
    
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)

# Test cases
print(process_input('Chang,Amy,1'))  # Invalid input format. Please provide input in the format 'string,string'.
print(process_input('Chang,Amy,2'))  # Invalid input format. Please provide input in the format 'string,string'.
print(process_input('Chang,Amy'))    # Invalid input format. Please provide input in the format 'string,string'.
print(process_input('Chang,Amy,3'))  # Invalid option. Please provide 1 or 2 as the second input.
print(process_input('Chang,Amy,1'))  # Amy
print(process_input('Chang,Amy,2'))  # Chang
print(process_input('smith,bobby,2'))  # Invalid input format. Please provide input in the format 'string,string'.
print(process_input('smith,bobby,1'))  # bobby

# End time: 2024-03-30 00:06:27.634130
# Elapsed time in seconds: 5.542576067999562