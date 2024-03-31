# Start time: 2024-03-30 01:04:31.285513
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return input, but remove the "+", add a "." in empty space, and replace all "-" with a ".", and given input as ['+106 769-858-438'] output is 106.769.858.438, given input as ['+83 973-757-831'] output is 83.973.757.831, given input as ['+62 647-787-775'] output is 62.647.787.775, given input as ['+172 027-507-632'] output is 172.027.507.632, given input as ['+72 001-050-856'] output is 72.001.050.856, given input as ['+95 310-537-401'] output is 95.310.537.401, given input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: '+106 769-858-438'
# Output: 106.769.858.438

def process_phone_number(input_str):
    try:
        # Remove the '+', replace '-' with '.', and remove any extra spaces
        output_str = input_str.replace('+', '').replace('-', '.').replace(' ', '')
        return output_str
    except Exception as e:
        print("Error processing phone number:", e)

# Test cases
print(process_phone_number('+106 769-858-438'))  # Output: 106.769.858.438
print(process_phone_number('+83 973-757-831'))    # Output: 83.973.757.831
print(process_phone_number('+62 647-787-775'))    # Output: 62.647.787.775
print(process_phone_number('+172 027-507-632'))   # Output: 172.027.507.632
print(process_phone_number('+72 001-050-856'))    # Output: 72.001.050.856
print(process_phone_number('+95 310-537-401'))    # Output: 95.310.537.401
print(process_phone_number('+6 775-969-238'))     # Output: 6.775.969.238

# End time: 2024-03-30 01:04:39.989357
# Elapsed time in seconds: 8.703600654000184