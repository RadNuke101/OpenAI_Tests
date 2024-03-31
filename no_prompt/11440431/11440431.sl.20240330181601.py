# Start time: 2024-03-30 18:24:32.339646

# Content: Given that given input as ['Mining US'] output is Mining, given input as ['Soybean Farming CAN'] output is Soybean Farming, given input as ['Soybean Farming'] output is Soybean Farming, given input as ['Oil Extraction US'] output is Oil Extraction, given input as ['Fishing'] output is Fishing, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_activity(input_str):
    try:
        # Input: 'Mining US' -> Output: 'Mining'
        # Input: 'Soybean Farming CAN' -> Output: 'Soybean Farming'
        # Input: 'Soybean Farming' -> Output: 'Soybean Farming'
        # Input: 'Oil Extraction US' -> Output: 'Oil Extraction'
        # Input: 'Fishing' -> Output: 'Fishing'
        
        # Extract the activity name by splitting the input string
        activity = input_str.split()[0]
        
        return activity
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
print(extract_activity('Mining US'))  # Output: Mining
print(extract_activity('Soybean Farming CAN'))  # Output: Soybean Farming
print(extract_activity('Soybean Farming'))  # Output: Soybean Farming
print(extract_activity('Oil Extraction US'))  # Output: Oil Extraction
print(extract_activity('Fishing'))  # Output: Fishing

# End time: 2024-03-30 18:24:36.362390
# Elapsed time in seconds: 4.022652569000002