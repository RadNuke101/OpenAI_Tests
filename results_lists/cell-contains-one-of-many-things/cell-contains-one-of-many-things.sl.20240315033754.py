def check_inputs(inputs):
    output = []
    for input_list in inputs:
        expression = input_list[0]
        words = input_list[1:]
        if any(word in expression for word in words):
            output.append('true')
        else:
            output.append('false')
    return output

input_data = [['yellow dog on green grass', 'yellow', 'green', 'dog'], ['warm gray sweater', 'yellow', 'green', 'dog'], ['A yellow sun in a green field', 'yellow', 'green', 'dog'], ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]
output_data = ['true', 'false', 'true', 'true']

assert check_inputs(input_data) == output_data
