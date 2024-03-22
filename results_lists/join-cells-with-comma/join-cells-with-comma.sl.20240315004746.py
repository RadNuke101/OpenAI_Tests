def process_inputs(inputs):
    result = []
    for input_list in inputs:
        output = ''
        for i in range(3):
            if input_list[i] != '':
                output += input_list[i]
                if i < 2:
                    output += ', '
        result.append(output)
    return result

inputs = [['figs', '', 'apples'], ['mangos', 'kiwis', 'grapes']]
output = process_inputs(inputs)
print(output)
