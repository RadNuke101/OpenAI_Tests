def check_inputs(inputs):
    output = []
    for input_list in inputs:
        expression = input_list[0]
        words = input_list[1:]
        if all(word in expression for word in words):
            output.append('true')
        else:
            output.append('false')
    return output

inputs = [['yellow dog on green grass', 'yellow', 'green', 'dog'], 
          ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'], 
          ['A yellow sun in a green field', 'yellow', 'green', 'dog'], 
          ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]

print(check_inputs(inputs))
