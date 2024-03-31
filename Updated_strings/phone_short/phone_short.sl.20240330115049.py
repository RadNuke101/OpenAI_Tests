# Start time: 2024-03-30 11:50:58.593690
# Content: Given that given input as ['938-242-504'] output is 938, given input as ['308-916-545'] output is 308, given input as ['623-599-749'] output is 623, given input as ['981-424-843'] output is 981, given input as ['118-980-214'] output is 118, given input as ['244-655-094'] output is 244, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input and output to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any noncode
def extract_first_number(phone_number):
    try:
        number = phone_number.split('-')[0]
        return int(number)
    except (IndexError, ValueError):
        return None

# Input: '938-242-504'
# Output: 938
# Input: '308-916-545'
# Output: 308
# Input: '623-599-749'
# Output: 623
# Input: '981-424-843'
# Output: 981
# Input: '118-980-214'
# Output: 118
# Input: '244-655-094'
# Output: 244

# End time: 2024-03-30 11:51:01.304857
# Elapsed time in seconds: 2.711113295999997