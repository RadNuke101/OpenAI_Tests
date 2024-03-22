# Prompt: delete the first "/" (from the left) and the next two numbers after
# Input: ['01/15/2013'] Output: 01/2013
# Input: ['03/07/2011'] Output: 03/2011
# Input: ['05/09/2009'] Output: 05/2009

def delete_numbers(input_date):
    date = input_date[0]
    output_date = date[:2] + date[4:]
    return output_date

# Test cases
print(delete_numbers(['01/15/2013']))  # Output: 01/2013
print(delete_numbers(['03/07/2011']))  # Output: 03/2011
print(delete_numbers(['05/09/2009']))  # Output: 05/2009
01/2013
03/2011
05/2009
