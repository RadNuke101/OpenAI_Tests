# Start time: 2024-03-30 02:11:38.411026
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove "Inc" and everything after from input, and given input as ['Trucking Inc.'] output is Trucking, given input as ['New Truck Inc'] output is New Truck, given input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove "Inc" and everything after from input
# Input: ['Trucking Inc.'] Output: Trucking
# Input: ['New Truck Inc'] Output: New Truck
# Input: ['ABV Trucking Inc, LLC'] Output: ABV Trucking

def remove_inc(input_str):
    try:
        # Remove "Inc" and everything after from input
        output_str = input_str.split(' Inc')[0]
        return output_str
    except:
        return "Invalid input"

# Test cases
print(remove_inc('Trucking Inc.'))  # Output: Trucking
print(remove_inc('New Truck Inc'))  # Output: New Truck
print(remove_inc('ABV Trucking Inc, LLC'))  # Output: ABV Trucking

# End time: 2024-03-30 02:11:44.340434
# Elapsed time in seconds: 5.929258882000795