def return_after_slash(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split("//")[1])
    return output_list

input_list = [['https=//exceljet.net/catalog'], ['https=//microsoft.com'], ['ftp=//someserver.com'], ['sftp=//127.0.0.1']]
print(return_after_slash(input_list))
