# Start time: 2024-03-30 02:22:29.510779
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete "miles" from input, and given input as ['736 miles'] output is 736, given input as ['1255 miles'] output is 1255, given input as ['1221 miles'] output is 1221, given input as ['790 miles'] output is 790, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete "miles" from input
# Input: ['736 miles']
# Output: 736

def extract_miles(input_str):
    try:
        miles_str = input_str.replace(" miles", "")
        miles = int(miles_str)
        return miles
    except:
        return "Invalid input"

# Test cases
print(extract_miles('736 miles'))  # Output: 736
print(extract_miles('1255 miles'))  # Output: 1255
print(extract_miles('1221 miles'))  # Output: 1221
print(extract_miles('790 miles'))  # Output: 790

# End time: 2024-03-30 02:22:33.115904
# Elapsed time in seconds: 3.6050456120010494