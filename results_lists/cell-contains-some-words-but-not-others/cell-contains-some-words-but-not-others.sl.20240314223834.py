def check_input(input_list):
    output = []
    for item in input_list:
        expression = item[0]
        words = item[1:]
        if any(word in expression for word in words):
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['red ball, green sweater', 'red', 'green', 'pink'], ['pink ball, green sweater', 'red', 'green', 'pink'], ['blue sea, pink ribbon', 'red', 'blue', 'pink'], ['black sea, white ribbon', 'red', 'blue', 'pink'], ['red green blue', 'red', 'blue', 'pink']]
output = check_input(input_list)
print(output)
