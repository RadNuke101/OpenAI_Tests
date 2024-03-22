def match_inputs(inputs):
    output = []
    for pair in inputs:
        if pair[0] == pair[1]:
            output.append('true')
        else:
            output.append('false')
    return output

# Test the function with the given input
inputs = [['apple', 'apple'], ['orange', 'Orange'], ['peach', 'peach'], ['cherry', 'cherrY']]
print(match_inputs(inputs))
