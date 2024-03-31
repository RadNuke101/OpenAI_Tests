# Start time: 2024-03-30 20:24:42.607851

# Content: Given that given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_name(input_str):
    try:
        name, index = input_str.split(',')
        index = int(index)
        
        if index == 1:
            return name.split(',')[1]
        elif index == 2:
            return name.split(',')[0]
        else:
            return "Invalid index, please enter 1 or 2"
    except ValueError:
        return "Invalid input format, please enter name,index as strings separated by a comma"

# Test cases
# print(get_name('Chang,Amy,1'))  # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('Chang,Amy,2'))  # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('Chang,Amy'))     # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('Chang,Amy,3'))   # Invalid index, please enter 1 or 2
# print(get_name('Chang,Amy,one')) # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('Chang,Amy,1'))   # Amy
# print(get_name('Chang,Amy,2'))   # Chang
# print(get_name('smith,bobby,2')) # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('smith,bobby,1')) # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('smith,bobby'))   # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('smith,bobby,3')) # Invalid index, please enter 1 or 2
# print(get_name('smith,bobby,one')) # Invalid input format, please enter name,index as strings separated by a comma
# print(get_name('smith,bobby,2')) # smith
# print(get_name('smith,bobby,1')) # bobby

# End time: 2024-03-30 20:24:51.340226
# Elapsed time in seconds: 8.732153713000116