# Prompt: return last three numbers in input
# given input as ['+106 769-858-438'] output is 438

def return_last_three(input_str):
    return input_str[-3:]

# Test cases
print(return_last_three('+106 769-858-438')) # 438
print(return_last_three('+83 973-757-831')) # 831
print(return_last_three('+62 647-787-775')) # 775
print(return_last_three('+172 027-507-632')) # 632
print(return_last_three('+72 001-050-856')) # 856
print(return_last_three('+95 310-537-401')) # 401
print(return_last_three('+6 775-969-238')) # 238
print(return_last_three('+174 594-539-946')) # 946
print(return_last_three('+155 927-275-860')) # 860
print(return_last_three('+167 405-461-331')) # 331
# Add more test cases if needed
