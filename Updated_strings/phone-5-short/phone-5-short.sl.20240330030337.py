# Start time: 2024-03-30 03:19:49.106082
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first three numbers in input, and given input as ['+106 769-858-438'] output is 106, given input as ['+83 973-757-831'] output is 83, given input as ['+62 647-787-775'] output is 62, given input as ['+172 027-507-632'] output is 172, given input as ['+72 001-050-856'] output is 72, given input as ['+95 310-537-401'] output is 95, given input as ['+6 775-969-238'] output is 6, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def get_first_number(input_str):
    try:
        input_str = input_str.strip()
        number = input_str.split()[0][1:]
        return number
    except:
        return "Invalid input"

# Prompt: return first three numbers in input
# Input: '+106 769-858-438'
# Output: '106'
# Input: '+83 973-757-831'
# Output: '83'
# Input: '+62 647-787-775'
# Output: '62'

# Test cases
print(get_first_number('+106 769-858-438'))  # Output: '106'
print(get_first_number('+83 973-757-831'))   # Output: '83'
print(get_first_number('+62 647-787-775'))   # Output: '62'

# End time: 2024-03-30 03:19:50.744842
# Elapsed time in seconds: 1.638712949001274