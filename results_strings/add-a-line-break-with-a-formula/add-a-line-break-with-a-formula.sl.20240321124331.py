# Prompt: add "/n" between the first and second inputted expression, and between the second and third inputted expression
# Input: ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']
# Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607

def format_address(input_list):
    return '/n'.join(input_list)

# Test the function with the provided inputs
input1 = ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']
input2 = ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933']
input3 = ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601']

print(format_address(input1))  # Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607
print(format_address(input2))  # Output: Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933
print(format_address(input3))  # Output: Linda Thomas/n2479 North Bend Road/nAllen, KY 41601
