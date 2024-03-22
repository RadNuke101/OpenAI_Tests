def extract_date(expression, num):
    if num == '1':
        return expression.split('-')[0]
    elif num == '2':
        return expression.split('-')[1]

# Input: '1/17/16-1/18/17', '1'
# Output: '1/17/16'
# Prompt: if second input (second column) is "1", return everything before "-" in expression
print(extract_date('1/17/16-1/18/17', '1'))

# Input: '1/17/16-1/18/17', '2'
# Output: '1/18/17'
# Prompt: if second input (second column) is "2", return everything after "-" in expression
print(extract_date('1/17/16-1/18/17', '2'))

# Input: '01/17/2016-01/18/2017', '1'
# Output: '01/17/2016'
# Prompt: if second input (second column) is "1", return everything before "-" in expression
print(extract_date('01/17/2016-01/18/2017', '1'))

# Input: '01/17/2016-01/18/2017', '2'
# Output: '01/18/2017'
# Prompt: if second input (second column) is "2", return everything after "-" in expression
print(extract_date('01/17/2016-01/18/2017', '2'))
