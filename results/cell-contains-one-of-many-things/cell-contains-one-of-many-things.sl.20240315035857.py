def check_inputs(input_list):
    output = []
    for input_data in input_list:
        expression = input_data[0]
        words = input_data[1:]
        if any(word in expression for word in words):
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['yellow dog on green grass', 'yellow', 'green', 'dog'], 
              ['warm gray sweater', 'yellow', 'green', 'dog'], 
              ['A yellow sun in a green field', 'yellow', 'green', 'dog'], 
              ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]

print(check_inputs(input_list))
