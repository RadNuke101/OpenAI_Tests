def check_input_in_expression(lst):
    result = []
    for item in lst:
        if item[1] in item[0]:
            result.append('true')
        else:
            result.append('false')
    return result

# Test the function with the given input
input_lst = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
output_lst = check_input_in_expression(input_lst)
print(output_lst)
