def check_color(input_list):
    output = []
    for color in input_list:
        if color[0] != 'gray' and color[0] != 'black':
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['yellow'], ['gray'], ['black'], ['blue'], ['pink'], ['orange'], ['turkey']]
output = check_color(input_list)
print(output)
