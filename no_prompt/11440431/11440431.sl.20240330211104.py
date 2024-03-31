# Start time: 2024-03-30 21:20:41.929293

# Content: Given that given input as ['Mining US'] output is Mining, given input as ['Soybean Farming CAN'] output is Soybean Farming, given input as ['Soybean Farming'] output is Soybean Farming, given input as ['Oil Extraction US'] output is Oil Extraction, given input as ['Fishing'] output is Fishing, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_activity(input_str):
    try:
        # Input: 'Mining US'
        # Output: 'Mining'
        activity = input_str.split()[0]
        return activity
    except IndexError:
        return "Invalid input format"
    except Exception as e:
        return str(e)

# Test cases
print(extract_activity('Mining US'))  # Output: Mining
print(extract_activity('Soybean Farming CAN'))  # Output: Soybean Farming
print(extract_activity('Soybean Farming'))  # Output: Soybean Farming
print(extract_activity('Oil Extraction US'))  # Output: Oil Extraction
print(extract_activity('Fishing'))  # Output: Fishing

# End time: 2024-03-30 21:20:44.006517
# Elapsed time in seconds: 2.0771460239993758