# Prompt: add "/n" between the first and second inputted expression, and between the second and third inputted expression
# Input: ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']
# Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607

def add_newline(input_list):
    return '/n'.join(input_list)

# Test the function with the provided inputs
input1 = ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']
output1 = add_newline(input1)
print(output1)

input2 = ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933']
output2 = add_newline(input2)
print(output2)

input3 = ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601']
output3 = add_newline(input3)
print(output3)
