def check_input(input_list):
    output = []
    for words, *expressions in input_list:
        if any(word in expressions for word in words.split()):
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['yellow dog on green grass', 'yellow', 'green', 'dog'], 
              ['warm gray sweater', 'yellow', 'green', 'dog'], 
              ['A yellow sun in a green field', 'yellow', 'green', 'dog'], 
              ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]

print(check_input(input_list))
