def process_input(input_list):
    output_list = []
    for item in input_list:
        file_name = item[0]
        file_name = file_name.split('.')[0]
        output_list.append(file_name)
    return output_list

input_list = [['happy.jpg'], ['pivot table.xls'], ['sales data.csv'], ['invoice3001.xls.pdf']]
output = process_input(input_list)
print(output)
