def return_after_slash(input_list):
    output_list = []
    for item in input_list:
        for sub_item in item:
            output_list.append(sub_item.split("//")[1])
    return output_list

input_list = [['https=//exceljet.net/catalog'], ['https=//microsoft.com'], ['ftp=//someserver.com'], ['sftp=//127.0.0.1']]
output = return_after_slash(input_list)
print(output)
