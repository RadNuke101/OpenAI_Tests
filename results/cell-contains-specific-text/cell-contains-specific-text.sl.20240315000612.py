def check_input(input_list):
    output = []
    for pair in input_list:
        if pair[1] in pair[0]:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['An apple a day keeps the doctor away', 'apple'], ['An apple a day keeps the doctor away', 'orange'], ['Better the devil you know', 'you know']]
print(check_input(input_list))
