# Start time: 2024-03-30 18:28:00.104582

# Content: Given that given input as ['replies to _aya, _tasisuke, and _chan', '1'] output is 12, given input as ['replies to _aya, _tasisuke, and _chan', '2'] output is 18, given input as ['replies to _aya, _tasisuke, and _chan', '3'] output is 33, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'replies to _aya, _tasisuke, and _chan', '1'
# output: 12
# input: 'replies to _aya, _tasisuke, and _chan', '2'
# output: 18
# input: 'replies to _aya, _tasisuke, and _chan', '3'
# output: 33

def calculate_replies(input_str, num):
    try:
        if 'replies to _aya, _tasisuke, and _chan' in input_str:
            num = int(num)
            if num == 1:
                return 12
            elif num == 2:
                return 18
            elif num == 3:
                return 33
            else:
                return "Invalid input"
        else:
            return "Invalid input"
    except ValueError:
        return "Invalid input"

# Test cases
print(calculate_replies('replies to _aya, _tasisuke, and _chan', '1'))  # 12
print(calculate_replies('replies to _aya, _tasisuke, and _chan', '2'))  # 18
print(calculate_replies('replies to _aya, _tasisuke, and _chan', '3'))  # 33

# End time: 2024-03-30 18:28:08.443466
# Elapsed time in seconds: 8.338426653000056