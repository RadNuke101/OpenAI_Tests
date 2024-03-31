# Start time: 2024-03-30 02:46:57.731705
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the three numbres in between "-" in input, and given input as ['+106 769-858-438'] output is 858, given input as ['+83 973-757-831'] output is 757, given input as ['+62 647-787-775'] output is 787, given input as ['+172 027-507-632'] output is 507, given input as ['+72 001-050-856'] output is 050, given input as ['+95 310-537-401'] output is 537, given input as ['+6 775-969-238'] output is 969, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the three numbers in between "-" in input
# Input: '+106 769-858-438'
# Output: '858'

def find_numbers_between_dash(input_str):
    try:
        # Split the input string by "-"
        parts = input_str.split('-')
        
        # Extract the middle number
        output = parts[1]
        
        return output
    except:
        return "Invalid input"

# Test cases
print(find_numbers_between_dash('+106 769-858-438'))  # Output: '858'
print(find_numbers_between_dash('+83 973-757-831'))    # Output: '757'
print(find_numbers_between_dash('+62 647-787-775'))    # Output: '787'
print(find_numbers_between_dash('+172 027-507-632'))   # Output: '507'
print(find_numbers_between_dash('+72 001-050-856'))    # Output: '050'
print(find_numbers_between_dash('+95 310-537-401'))    # Output: '537'
print(find_numbers_between_dash('+6 775-969-238'))     # Output: '969'

# End time: 2024-03-30 02:47:00.592777
# Elapsed time in seconds: 2.8610121780002373