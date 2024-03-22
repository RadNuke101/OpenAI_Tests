def match_inputs(input_list):
    output = []
    for pair in input_list:
        if pair[0] == pair[1]:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['apple', 'apple'], ['orange', 'Orange'], ['peach', 'peach'], ['cherry', 'cherrY']]
print(match_inputs(input_list))
