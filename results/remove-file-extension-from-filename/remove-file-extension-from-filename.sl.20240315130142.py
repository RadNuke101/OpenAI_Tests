def delete_period(input):
    output = []
    for item in input:
        output.append(item[0].split('.')[0])
    return output

input = [['happy.jpg'], ['pivot table.xls'], ['sales data.csv'], ['invoice3001.xls.pdf']]
output = delete_period(input)
print(output)
