def check_for_9999999(input_list):
    output = []
    for item in input_list:
        if '9999999' in item[0]:
            output.append('true')
        else:
            output.append('false')
    return output

input_list = [['dhfjd9999999dfda'], ['ddsss999dfdfsfd']]
print(check_for_9999999(input_list))
