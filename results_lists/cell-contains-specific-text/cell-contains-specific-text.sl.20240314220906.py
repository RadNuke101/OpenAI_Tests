def check_input(expression_list):
    output = []
    for expression, word in expression_list:
        if word in expression:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
output_list = check_input(input_list)
print(output_list)
