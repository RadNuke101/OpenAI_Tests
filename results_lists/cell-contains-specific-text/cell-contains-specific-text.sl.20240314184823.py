def check_input_in_expression(input_list):
    output = []
    for expression, word in input_list:
        if word in expression:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
print(check_input_in_expression(input_list))
