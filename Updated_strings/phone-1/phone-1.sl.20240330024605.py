# Start time: 2024-03-30 03:00:02.319033
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the three numbers between the "-", and given input as ['938-242-504'] output is 242, given input as ['308-916-545'] output is 916, given input as ['623-599-749'] output is 599, given input as ['981-424-843'] output is 424, given input as ['118-980-214'] output is 980, given input as ['244-655-094'] output is 655, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the three numbers between the "-", 
# Input: '938-242-504'
# Output: 242

def get_number_between_dash(input_str):
    try:
        # Split the input string by "-"
        numbers = input_str.split('-')
        
        # Return the second element
        return numbers[1]
    except:
        return "Invalid input"

# Test cases
print(get_number_between_dash('938-242-504'))  # Output: 242
print(get_number_between_dash('308-916-545'))  # Output: 916
print(get_number_between_dash('623-599-749'))  # Output: 599
print(get_number_between_dash('981-424-843'))  # Output: 424
print(get_number_between_dash('118-980-214'))  # Output: 980
print(get_number_between_dash('244-655-094'))  # Output: 655

# End time: 2024-03-30 03:00:06.259243
# Elapsed time in seconds: 3.940100514999358