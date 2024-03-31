# Start time: 2024-03-30 20:35:19.420788

# Content: Given that given input as ['some project,other project'] output is true, given input as ['some project'] output is true, given input as ['overhead'] output is false, given input as ['some project, overhead'] output is false, given input as ['some project, other, boo'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'some project,other project' -> output: True
# input: 'some project' -> output: True
# input: 'overhead' -> output: False
# input: 'some project, overhead' -> output: False
# input: 'some project, other, boo' -> output: True

def check_projects(input_str):
    try:
        projects = input_str.split(',')
        for project in projects:
            if 'project' in project.strip():
                return True
        return False
    except Exception as e:
        return False

# Test cases
print(check_projects('some project,other project'))  # True
print(check_projects('some project'))  # True
print(check_projects('overhead'))  # False
print(check_projects('some project, overhead'))  # False
print(check_projects('some project, other, boo'))  # True

# End time: 2024-03-30 20:35:21.074268
# Elapsed time in seconds: 1.653794435999771