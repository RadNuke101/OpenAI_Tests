# Prompt: if second input is 1, return everything after the ",", else if the second input is 2, return everything before the ","
# Input: ['Chang,Amy', '1'] Output: Amy
# Input: ['Chang,Amy', '2'] Output: Chang
# Input: ['smith,bobby', '2'] Output: smith
# Input: ['smith,bobby', '1'] Output: bobby

def process_input(input_str):
    input_list = input_str.split(',')
    if input_list[1] == '1':
        return input_list[1]
    elif input_list[1] == '2':
        return input_list[0]

# Test cases
print(process_input('Chang,Amy,1'))  # Output: Amy
print(process_input('Chang,Amy,2'))  # Output: Chang
print(process_input('smith,bobby,2'))  # Output: smith
print(process_input('smith,bobby,1'))  # Output: bobby
