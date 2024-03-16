def check_input(inputs):
    output = []
    for pair in inputs:
        if pair[1] in pair[0]:
            output.append('true')
        else:
            output.append('false')
    return output

inputs = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
print(check_input(inputs))
