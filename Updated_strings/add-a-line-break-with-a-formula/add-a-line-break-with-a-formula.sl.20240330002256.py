# Start time: 2024-03-30 00:24:57.157319
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: add "/n" between the first and second inputted expression, and between the second and third inputted expression, and given input as ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607'] output is Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607, given input as ['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933'] output is Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933, given input as ['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601'] output is Linda Thomas/n2479 North Bend Road/nAllen, KY 41601, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: add "/n" between the first and second inputted expression, and between the second and third inputted expression
# Input: ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']
# Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607

def format_address(input_data):
    try:
        if len(input_data) != 3:
            raise ValueError("Input should contain exactly 3 elements")
        
        formatted_address = "/n".join(input_data)
        return formatted_address
    except Exception as e:
        return str(e)

# Test cases
print(format_address(['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']))  # Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607
print(format_address(['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933']))  # Output: Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933
print(format_address(['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601']))  # Output: Linda Thomas/n2479 North Bend Road/nAllen, KY 41601

# End time: 2024-03-30 00:25:05.995599
# Elapsed time in seconds: 8.838236857000084