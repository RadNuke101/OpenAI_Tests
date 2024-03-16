def delete_period(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('.')[0])
    return output_list

input_list = [['happy.jpg'], ['pivot table.xls'], ['sales data.csv'], ['invoice3001.xls.pdf']]
output = delete_period(input_list)
print(output)
