def check_inputs(input_list):
    output = []
    for item in input_list:
        first_words = item[0].split()[:2]
        if item[1] in first_words or item[2] in first_words or item[3] in first_words:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['yellow dog on green grass', 'yellow', 'green', 'cat'], 
              ['warm gray sweater', 'yellow', 'green', 'cat'], 
              ['blue neon signs', 'blue', 'green', 'neon'], 
              ['hot pink socks', 'blue', 'pink', 'neon'], 
              ['deep black eyes', 'yellow', 'green', 'neon']]

print(check_inputs(input_list))
