# Start time: 2024-03-30 04:03:26.866808
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last three numbers in input, and given input as ['+106 769-858-438'] output is 438, given input as ['+83 973-757-831'] output is 831, given input as ['+62 647-787-775'] output is 775, given input as ['+172 027-507-632'] output is 632, given input as ['+72 001-050-856'] output is 856, given input as ['+95 310-537-401'] output is 401, given input as ['+6 775-969-238'] output is 238, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return last three numbers in input
# Input: '+106 769-858-438'
# Output: '438'

def return_last_three(input_str):
    try:
        input_str = input_str.replace(' ', '')  # Remove spaces
        output = input_str[-3:]  # Get last three characters
        return output
    except:
        return "Invalid input"

# Test cases
print(return_last_three('+106 769-858-438'))  # Output: '438'
print(return_last_three('+83 973-757-831'))   # Output: '831'
print(return_last_three('+62 647-787-775'))   # Output: '775'
print(return_last_three('+172 027-507-632'))  # Output: '632'
print(return_last_three('+72 001-050-856'))   # Output: '856'
print(return_last_three('+95 310-537-401'))   # Output: '401'
print(return_last_three('+6 775-969-238'))    # Output: '238'

# End time: 2024-03-30 04:03:31.485609
# Elapsed time in seconds: 4.618694118998974