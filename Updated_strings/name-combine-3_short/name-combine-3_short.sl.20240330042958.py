# Start time: 2024-03-30 04:44:07.326117
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first input, followed by a period and a space, and then the second input, and given input as ['Launa', 'Withers'] output is L. Withers, given input as ['Lakenya', 'Edison'] output is L. Edison, given input as ['Brendan', 'Hage'] output is B. Hage, given input as ['Bradford', 'Lango'] output is B. Lango, given input as ['Rudolf', 'Akiyama'] output is R. Akiyama, given input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def get_formatted_name(input_str):
    try:
        input_list = input_str.split(', ')
        first_letter = input_list[0][0]
        formatted_name = first_letter + '. ' + input_list[1]
        return formatted_name
    except (IndexError, AttributeError):
        return "Invalid input format. Please provide two strings separated by a comma and a space."

# Input: "Launa, Withers"
# Output: "L. Withers"
# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: "Lakenya, Edison"
# Output: "L. Edison"
# Input: "Brendan, Hage"
# Output: "B. Hage"
# Input: "Bradford, Lango"
# Output: "B. Lango"
# Input: "Rudolf, Akiyama"
# Output: "R. Akiyama"
# Input: "Lara, Constable"
# Output: "L. Constable"

# Test the function with sample inputs
print(get_formatted_name("Launa, Withers"))
print(get_formatted_name("Lakenya, Edison"))
print(get_formatted_name("Brendan, Hage"))
print(get_formatted_name("Bradford, Lango"))
print(get_formatted_name("Rudolf, Akiyama"))
print(get_formatted_name("Lara, Constable"))

# End time: 2024-03-30 04:44:12.683243
# Elapsed time in seconds: 5.357105168997805