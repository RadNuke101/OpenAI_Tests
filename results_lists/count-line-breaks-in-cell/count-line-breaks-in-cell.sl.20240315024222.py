def count_newlines(lst):
    return [str(item[0].count('/n') + 1) for item in lst]

input_lst = [['one'], ['one/ntwo'], ['one/ntwo/nthree']]
output_lst = count_newlines(input_lst)
print(output_lst)
