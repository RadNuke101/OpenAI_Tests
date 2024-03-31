# Start time: 2024-03-30 00:30:25.861027
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_com_phrase(input_str):
    try:
        phrase = input_str.split()  # Split the input string into words
        for word in phrase:
            if word.endswith(".com"):
                return word.strip()  # Return the word with ".com" at the end
    except Exception as e:
        print("Error: ", e)
    
    return None

# Test cases
input1 = 'send email to json_acme.com'
input2 = 'contact help_robot.com for all support requests'

output1 = find_com_phrase(input1)
output2 = find_com_phrase(input2)

print(output1)  # Output: json_acme.com
print(output2)  # Output: help_robot.com

# End time: 2024-03-30 00:30:30.388008
# Elapsed time in seconds: 4.526933219000057