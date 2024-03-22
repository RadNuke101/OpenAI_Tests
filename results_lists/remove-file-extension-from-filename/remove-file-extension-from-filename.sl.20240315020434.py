def remove_file_extension(input_list):
    output_list = []
    for item in input_list:
        file_name = item[0]
        if '.' in file_name:
            file_name = file_name.split('.')[0]
        output_list.append(file_name)
    return output_list

input_list = [['happy.jpg'], ['pivot table.xls'], ['sales data.csv'], ['invoice3001.xls.pdf']]
print(remove_file_extension(input_list))
