# Start time: 2024-03-30 02:48:30.835171
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove "Inc" and everything after from input, and given input as ['Trucking Inc.'] output is Trucking, given input as ['New Truck Inc'] output is New Truck, given input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove "Inc" and everything after from input
# input: 'Trucking Inc.', output: 'Trucking'
# input: 'New Truck Inc', output: 'New Truck'
# input: 'ABV Trucking Inc, LLC', output: 'ABV Trucking'

def remove_suffix(input_str):
    try:
        # Remove "Inc" and everything after it
        output_str = input_str.split(' Inc')[0]
        return output_str
    except:
        return "Invalid input"

# Test cases
print(remove_suffix('Trucking Inc.'))  # Output: Trucking
print(remove_suffix('New Truck Inc'))  # Output: New Truck
print(remove_suffix('ABV Trucking Inc, LLC'))  # Output: ABV Trucking

# End time: 2024-03-30 02:48:33.791431
# Elapsed time in seconds: 2.9562125880001986