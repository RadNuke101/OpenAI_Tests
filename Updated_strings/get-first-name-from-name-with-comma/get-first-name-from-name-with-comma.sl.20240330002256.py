# Start time: 2024-03-30 00:24:06.991197
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input is 1, return everything after the ",". else if the second input is 2, return everything before the ",", and given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if second input is 1, return everything after the ",", else if the second input is 2, return everything before the ","
# Input: ['Chang,Amy', '1'] Output: Amy
# Input: ['Chang,Amy', '2'] Output: Chang
# Input: ['smith,bobby', '2'] Output: smith
# Input: ['smith,bobby', '1'] Output: bobby

def process_input(input_list):
    try:
        input_str = input_list[0]
        option = int(input_list[1])

        if option == 1:
            output = input_str.split(',')[1]
        elif option == 2:
            output = input_str.split(',')[0]
        else:
            output = "Invalid option, please provide 1 or 2 as the second input."

        return output

    except IndexError:
        return "Input list must contain two elements."
    except ValueError:
        return "Second input must be a valid integer."

# Test cases
print(process_input(['Chang,Amy', '1']))  # Output: Amy
print(process_input(['Chang,Amy', '2']))  # Output: Chang
print(process_input(['smith,bobby', '2']))  # Output: smith
print(process_input(['smith,bobby', '1']))  # Output: bobby

# End time: 2024-03-30 00:24:13.194265
# Elapsed time in seconds: 6.203040527000212