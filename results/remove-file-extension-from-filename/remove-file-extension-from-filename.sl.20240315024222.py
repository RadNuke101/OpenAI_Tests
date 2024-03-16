def process_input(input_list):
    output_list = []
    for item in input_list:
        filename = item[0]
        if '.' in filename:
            filename = filename.split('.')[0]
        output_list.append(filename)
    return output_list

input_list = [['happy.jpg'], ['pivot table.xls'], ['sales data.csv'], ['invoice3001.xls.pdf']]
print(process_input(input_list))
