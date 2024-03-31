# Start time: 2024-03-30 01:41:22.805015
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last three numbers in input, and given input as ['+106 769-858-438'] output is 438, given input as ['+83 973-757-831'] output is 831, given input as ['+62 647-787-775'] output is 775, given input as ['+172 027-507-632'] output is 632, given input as ['+72 001-050-856'] output is 856, given input as ['+95 310-537-401'] output is 401, given input as ['+6 775-969-238'] output is 238, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def return_last_three_numbers(input_str):
    try:
        # Prompt: return last three numbers in input
        # Input: ['+106 769-858-438'], Output: 438
        # Input: ['+83 973-757-831'], Output: 831
        # Input: ['+62 647-787-775'], Output: 775
        # Input: ['+172 027-507-632'], Output: 632
        # Input: ['+72 001-050-856'], Output: 856
        # Input: ['+95 310-537-401'], Output: 401
        # Input: ['+6 775-969-238'], Output: 238
        
        # Extract the last three numbers from the input string
        last_three_numbers = input_str[-3:]
        
        return last_three_numbers
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(return_last_three_numbers('+106 769-858-438'))  # Output: 438
print(return_last_three_numbers('+83 973-757-831'))   # Output: 831
print(return_last_three_numbers('+62 647-787-775'))   # Output: 775
print(return_last_three_numbers('+172 027-507-632'))  # Output: 632
print(return_last_three_numbers('+72 001-050-856'))   # Output: 856
print(return_last_three_numbers('+95 310-537-401'))   # Output: 401
print(return_last_three_numbers('+6 775-969-238'))    # Output: 238

# End time: 2024-03-30 01:41:29.151512
# Elapsed time in seconds: 6.346369691000291