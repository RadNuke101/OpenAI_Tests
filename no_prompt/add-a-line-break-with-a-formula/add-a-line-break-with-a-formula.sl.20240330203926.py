# Start time: 2024-03-30 20:41:18.426770

# Content: Given that given input as ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607'] output is Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607, given input as ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933'] output is Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933, given input as ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601'] output is Linda Thomas/n2479 North Bend Road/nAllen, KY 41601, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_address(input_str):
    try:
        input_list = input_str.split(', ')
        name = input_list[0]
        address = input_list[1] + '/n' + input_list[2] + '/n' + input_list[3]
        return name + '/n' + address
    except IndexError:
        return "Invalid input format. Please provide name, street address, city, and zip code separated by commas."

# Test cases
print(format_address('Traci Brown, 1301 Robinson Court, Saginaw, MI 48607'))
print(format_address('Mary Hannan, 1195 Amethyst Drive, Lansing, MI 48933'))
print(format_address('Linda Thomas, 2479 North Bend Road, Allen, KY 41601'))
Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607
Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933
Linda Thomas/n2479 North Bend Road/nAllen, KY 41601

# End time: 2024-03-30 20:41:20.179844
# Elapsed time in seconds: 1.7530359530001078