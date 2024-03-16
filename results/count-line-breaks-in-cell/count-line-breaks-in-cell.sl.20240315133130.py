def count_newlines(input_list):
    output_list = []
    for expression in input_list:
        count = expression[0].count('/n') + 1
        output_list.append(str(count))
    return output_list

input_list = [['one'], ['one/ntwo'], ['one/ntwo/nthree']]
print(count_newlines(input_list))
