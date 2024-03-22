def check_inputs(inputs):
    output = []
    for input_list in inputs:
        if all(word in input_list[0] for word in input_list[1:]):
            output.append('true')
        else:
            output.append('false')
    return output

inputs = [['yellow dog on green grass', 'yellow', 'green', 'dog'], 
          ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'], 
          ['A yellow sun in a green field', 'yellow', 'green', 'dog'], 
          ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]
output = check_inputs(inputs)
print(output)
