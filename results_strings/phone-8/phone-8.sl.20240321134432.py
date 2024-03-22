# Prompt: return last three numbers in input
# Input: ['+106 769-858-438']
# Output: 438

def return_last_three(input_str):
    return input_str[-3:]

# Test cases
print(return_last_three('+106 769-858-438'))  # Output: 438
print(return_last_three('+83 973-757-831'))   # Output: 831
print(return_last_three('+62 647-787-775'))   # Output: 775
print(return_last_three('+172 027-507-632'))  # Output: 632
print(return_last_three('+72 001-050-856'))   # Output: 856
print(return_last_three('+95 310-537-401'))   # Output: 401
print(return_last_three('+6 775-969-238'))    # Output: 238
