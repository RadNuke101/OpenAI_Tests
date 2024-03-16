def check_color(input_list):
    output_list = []
    for color in input_list:
        if color[0] != 'gray' and color[0] != 'black':
            output_list.append('true')
        else:
            output_list.append('false')
    return output_list

input_list = [['yellow'], ['gray'], ['black'], ['blue'], ['pink'], ['orange'], ['turkey']]
output = check_color(input_list)
print(output)
