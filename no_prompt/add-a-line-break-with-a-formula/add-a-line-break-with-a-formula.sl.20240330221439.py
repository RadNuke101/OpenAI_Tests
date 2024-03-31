# Start time: 2024-03-30 22:16:15.025188

# Content: Given that given input as ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607'] output is Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607, given input as ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933'] output is Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933, given input as ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601'] output is Linda Thomas/n2479 North Bend Road/nAllen, KY 41601, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_address(input_str):
    try:
        input_list = input_str.split(',')
        name = input_list[0].strip()
        address = input_list[1].strip()
        city_state_zip = input_list[2].strip()
        
        output_str = f"{name}\n{address}\n{city_state_zip}"
        return output_str
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(format_address('Traci Brown, 1301 Robinson Court, Saginaw, MI 48607'))  # Traci Brown\n1301 Robinson Court\nSaginaw, MI 48607
print(format_address('Mary Hannan, 1195 Amethyst Drive, Lansing, MI 48933'))  # Mary Hannan\n1195 Amethyst Drive\nLansing, MI 48933
print(format_address('Linda Thomas, 2479 North Bend Road, Allen, KY 41601'))  # Linda Thomas\n2479 North Bend Road\nAllen, KY 41601

# End time: 2024-03-30 22:16:18.000863
# Elapsed time in seconds: 2.9755913669996517