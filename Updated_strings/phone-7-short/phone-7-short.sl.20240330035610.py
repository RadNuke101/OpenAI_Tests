# Start time: 2024-03-30 04:03:45.809522
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the three numbres in between "-" in input, and given input as ['+106 769-858-438'] output is 858, given input as ['+83 973-757-831'] output is 757, given input as ['+62 647-787-775'] output is 787, given input as ['+172 027-507-632'] output is 507, given input as ['+72 001-050-856'] output is 050, given input as ['+95 310-537-401'] output is 537, given input as ['+6 775-969-238'] output is 969, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the three numbers in between "-" in input
# Input: '+106 769-858-438'
# Output: '858'

def find_numbers_between_hyphens(input_str):
    try:
        # Extract the numbers between the hyphens
        numbers = input_str.split('-')[1:-1]
        
        # Return the numbers as a string
        return ''.join(numbers)
    
    except Exception as e:
        return str(e)

# Test cases
print(find_numbers_between_hyphens('+106 769-858-438'))  # Output: '858'
print(find_numbers_between_hyphens('+83 973-757-831'))    # Output: '757'
print(find_numbers_between_hyphens('+62 647-787-775'))    # Output: '787'
print(find_numbers_between_hyphens('+172 027-507-632'))   # Output: '507'
print(find_numbers_between_hyphens('+72 001-050-856'))    # Output: '050'
print(find_numbers_between_hyphens('+95 310-537-401'))    # Output: '537'
print(find_numbers_between_hyphens('+6 775-969-238'))     # Output: '969'

# End time: 2024-03-30 04:03:52.768672
# Elapsed time in seconds: 6.958991075000085