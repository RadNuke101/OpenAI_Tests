def count_newlines(input_list):
    output_list = []
    for item in input_list:
        count = item[0].count("/n") + 1
        output_list.append(str(count))
    return output_list

input_list = [['one'], ['one/ntwo'], ['one/ntwo/nthree']]
output_list = count_newlines(input_list)
print(output_list)
