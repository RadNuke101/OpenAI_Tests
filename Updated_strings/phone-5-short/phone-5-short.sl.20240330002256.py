# Start time: 2024-03-30 00:39:35.402085
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first three numbers in input, and given input as ['+106 769-858-438'] output is 106, given input as ['+83 973-757-831'] output is 83, given input as ['+62 647-787-775'] output is 62, given input as ['+172 027-507-632'] output is 172, given input as ['+72 001-050-856'] output is 72, given input as ['+95 310-537-401'] output is 95, given input as ['+6 775-969-238'] output is 6, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return first three numbers in input
# Input: '+106 769-858-438'
# Output: 106

def extract_first_three_numbers(input_str):
    try:
        number = input_str.split()[0][1:]  # Extracting the first three numbers after '+'
        return int(number)
    except:
        return "Invalid input"

# Test cases
print(extract_first_three_numbers('+106 769-858-438'))  # Output: 106
print(extract_first_three_numbers('+83 973-757-831'))    # Output: 83
print(extract_first_three_numbers('+62 647-787-775'))    # Output: 62
print(extract_first_three_numbers('+172 027-507-632'))   # Output: 172
print(extract_first_three_numbers('+72 001-050-856'))    # Output: 72
print(extract_first_three_numbers('+95 310-537-401'))    # Output: 95
print(extract_first_three_numbers('+6 775-969-238'))     # Output: 6

# End time: 2024-03-30 00:39:40.087894
# Elapsed time in seconds: 4.685761649000597