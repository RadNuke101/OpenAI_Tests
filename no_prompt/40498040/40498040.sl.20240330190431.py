# Start time: 2024-03-30 19:15:18.705420

# Content: Given that given input as ['some project,other project'] output is true, given input as ['some project'] output is true, given input as ['overhead'] output is false, given input as ['some project, overhead'] output is false, given input as ['some project, other, boo'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_projects(input_str):
    try:
        projects = input_str.split(',')
        for project in projects:
            if 'overhead' in project:
                return False
        return True
    except Exception as e:
        print("Error: Invalid input format")

# Test cases
# Input: 'some project,other project' => Output: True
# Input: 'some project' => Output: True
# Input: 'overhead' => Output: False
# Input: 'some project, overhead' => Output: False
# Input: 'some project, other, boo' => Output: True

# End time: 2024-03-30 19:15:20.237790
# Elapsed time in seconds: 1.5323257639997792