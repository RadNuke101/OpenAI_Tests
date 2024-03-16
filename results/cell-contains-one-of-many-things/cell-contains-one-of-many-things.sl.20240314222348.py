def check_inputs(inputs):
    outputs = []
    for input_list in inputs:
        expression = input_list[0]
        words = input_list[1:]
        if any(word in expression for word in words):
            outputs.append('true')
        else:
            outputs.append('false')
    return outputs

inputs = [['yellow dog on green grass', 'yellow', 'green', 'dog'], 
          ['warm gray sweater', 'yellow', 'green', 'dog'], 
          ['A yellow sun in a green field', 'yellow', 'green', 'dog'], 
          ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]
output = ['true', 'false', 'true', 'true']

assert check_inputs(inputs) == output
