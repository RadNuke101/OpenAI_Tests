def check_inputs(inputs):
    output = []
    for input_list in inputs:
        first_words = input_list[0].split()[:2]
        if input_list[1] in first_words or input_list[2] in first_words or input_list[3] in first_words:
            output.append('true')
        else:
            output.append('false')
    return output

inputs = [['yellow dog on green grass', 'yellow', 'green', 'cat'], 
          ['warm gray sweater', 'yellow', 'green', 'cat'], 
          ['blue neon signs', 'blue', 'green', 'neon'], 
          ['hot pink socks', 'blue', 'pink', 'neon'], 
          ['deep black eyes', 'yellow', 'green', 'neon']]

print(check_inputs(inputs))
