def extract_date(input_str):
    input_list = input_str.split(',')
    expression = input_list[0]
    option = input_list[1]
    
    if option == '1':
        return expression.split('-')[0]
    elif option == '2':
        return expression.split('-')[1]

# Prompt: if second input (second column) is "1", return everything before "-" in expression, else if second input is "2", return everything after "-" in expression
# Input: ['1/17/16-1/18/17', '1']
# Output: 1/17/16
# Input: ['1/17/16-1/18/17', '2']
# Output: 1/18/17
# Input: ['01/17/2016-01/18/2017', '1']
# Output: 01/17/2016
# Input: ['01/17/2016-01/18/2017', '2']
# Output: 01/18/2017
