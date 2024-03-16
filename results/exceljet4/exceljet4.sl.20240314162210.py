def extract_domain(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split("//")[1])
    return output_list

input_list = [['https=//exceljet.net/catalog'], ['https=//microsoft.com'], ['ftp=//someserver.com'], ['sftp=//127.0.0.1']]
print(extract_domain(input_list))
