def check_input_output(input_data):
    output = []
    for data in input_data:
        expression = data[0]
        words = data[1:]
        if any(word in expression for word in words):
            output.append('true')
        else:
            output.append('false')
    return output

input_data = [['red ball, green sweater', 'red', 'green', 'pink'], 
              ['pink ball, green sweater', 'red', 'green', 'pink'], 
              ['blue sea, pink ribbon', 'red', 'blue', 'pink'], 
              ['black sea, white ribbon', 'red', 'blue', 'pink'], 
              ['red green blue', 'red', 'blue', 'pink']]

print(check_input_output(input_data))
