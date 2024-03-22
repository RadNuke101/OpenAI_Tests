def process_inputs(inputs):
    result = []
    for input_list in inputs:
        output = ''
        for i in range(3):
            if input_list[i] != '':
                output += input_list[i]
                if i < 2 and input_list[i+1] != '':
                    output += ', '
        result.append(output)
    return result

# Test the function with the given input
inputs = [['figs', '', 'apples'], ['mangos', 'kiwis', 'grapes']]
output = process_inputs(inputs)
print(output)
