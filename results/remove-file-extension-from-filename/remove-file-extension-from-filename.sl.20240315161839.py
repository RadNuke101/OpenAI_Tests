def clean_filenames(input_list):
    output_list = []
    for item in input_list:
        filename = item[0].split('.')[0]
        output_list.append(filename)
    return output_list

# Test the function
input_list = [['happy.jpg'], ['pivot table.xls'], ['sales data.csv'], ['invoice3001.xls.pdf']]
print(clean_filenames(input_list))
