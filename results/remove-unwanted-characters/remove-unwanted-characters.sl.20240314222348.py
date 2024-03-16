def remove_second_input(input_list):
    output = []
    for i in range(len(input_list)):
        output.append(input_list[i][0].replace(input_list[i][1], "", 1))
    return output

input_list = [['zx66448', 'z'], ['zx66448', 'x'], ['zx66448', '6'], ['zx66448', '4'], ['zx66448', '8']]
print(remove_second_input(input_list))
