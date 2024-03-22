def check_input(expression):
    output = []
    for exp, word in expression:
        if word in exp:
            output.append('true')
        else:
            output.append('false')
    return output

input_data = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
print(check_input(input_data))
