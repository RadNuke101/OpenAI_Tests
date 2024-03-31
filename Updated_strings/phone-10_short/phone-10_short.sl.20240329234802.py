# Start time: 2024-03-30 00:04:42.248802
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space, and given input as ['+106 769-858-438'] output is +106 (769) 858-438, given input as ['+83 973-757-831'] output is +83 (973) 757-831, given input as ['+62 647-787-775'] output is +62 (647) 787-775, given input as ['+172 027-507-632'] output is +172 (027) 507-632, given input as ['+72 001-050-856'] output is +72 (001) 050-856, given input as ['+95 310-537-401'] output is +95 (310) 537-401, given input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def format_phone_number(input_str):
    try:
        input_str = input_str.strip()
        parts = input_str.split('-')
        first_three_nums = parts[0][:3]
        output = input_str.replace('-', ' ', 1).replace(first_three_nums, f'({first_three_nums})', 1)
        return output
    except Exception as e:
        return f"Error: {e}"

# Input: '+106 769-858-438'
# Output: +106 (769) 858-438
# Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space

# Test cases
print(format_phone_number('+106 769-858-438'))
print(format_phone_number('+83 973-757-831'))
print(format_phone_number('+62 647-787-775'))
print(format_phone_number('+172 027-507-632'))
print(format_phone_number('+72 001-050-856'))
print(format_phone_number('+95 310-537-401'))
print(format_phone_number('+6 775-969-238'))

# End time: 2024-03-30 00:04:44.595320
# Elapsed time in seconds: 2.346435038999971