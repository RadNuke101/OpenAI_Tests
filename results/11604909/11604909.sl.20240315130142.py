def extract_first_decimal(input_list):
    output = []
    for item in input_list:
        for word in item[0].split():
            if '.' in word:
                decimal = word.split('.')[0] + '.' + word.split('.')[1][0]
                output.append(decimal)
                break
    return output

input_list = [['AIX 5.1'], ['VMware ESX Server 3.5.0 build-110268'], ['Linux Linux 2.6 Linux'], ['Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'], ['Microsoft <R> Windows <R> 2000 Advanced Server 1.0'], ['Microsoft Windows XP Win2008R2 6.1.7601']]
print(extract_first_decimal(input_list))