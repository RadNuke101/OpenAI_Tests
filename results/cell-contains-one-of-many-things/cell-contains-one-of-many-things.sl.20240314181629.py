def check_inputs(input_list):
    output = []
    for item in input_list:
        expression = item[0]
        words = item[1:]
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
