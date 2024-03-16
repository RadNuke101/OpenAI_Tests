def return_after_slash(input_list):
    output = []
    for item in input_list:
        for sub_item in item:
            output.append(sub_item.split("//")[1])
    return output

input_list = [['https=//exceljet.net/catalog'], ['https=//microsoft.com'], ['ftp=//someserver.com'], ['sftp=//127.0.0.1']]
print(return_after_slash(input_list))
