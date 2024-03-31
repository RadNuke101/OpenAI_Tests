# Start time: 2024-03-30 00:08:03.950710
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove "Inc" and everything after from input, and given input as ['Trucking Inc.'] output is Trucking, given input as ['New Truck Inc'] output is New Truck, given input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove "Inc" and everything after from input
# Input: 'Trucking Inc.' Output: 'Trucking'
# Input: 'New Truck Inc' Output: 'New Truck'
# Input: 'ABV Trucking Inc, LLC' Output: 'ABV Trucking'

def remove_suffix(input_str):
    try:
        if 'Inc' in input_str:
            output = input_str.split('Inc')[0].strip()
        else:
            output = input_str
        return output
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(remove_suffix('Trucking Inc.'))  # Output: Trucking
print(remove_suffix('New Truck Inc'))  # Output: New Truck
print(remove_suffix('ABV Trucking Inc, LLC'))  # Output: ABV Trucking

# End time: 2024-03-30 00:08:05.532404
# Elapsed time in seconds: 1.5816487080001025