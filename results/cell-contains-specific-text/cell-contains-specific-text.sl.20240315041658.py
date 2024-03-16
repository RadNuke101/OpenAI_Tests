def check_input(inputs):
    output = []
    for expression, word in inputs:
        if word in expression:
            output.append('true')
        else:
            output.append('false')
    return output

inputs = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
print(check_input(inputs))
