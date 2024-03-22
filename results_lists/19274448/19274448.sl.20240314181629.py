def check_for_9999999(input_list):
    output_list = []
    for item in input_list:
        if '9999999' in item[0]:
            output_list.append('true')
        else:
            output_list.append('false')
    return output_list

input_list = [['dhfjd9999999dfda'], ['ddsss999dfdfsfd']]
print(check_for_9999999(input_list))
