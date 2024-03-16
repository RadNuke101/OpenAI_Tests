def first_decimal_to_tenths(input_list):
    output = []
    for item in input_list:
        for i in item:
            decimal = ''
            for char in i:
                if char.isdigit() or char == '.':
                    decimal += char
                elif decimal:
                    break
            output.append(decimal)
    return output

input_list = [['AIX 5.1'], ['VMware ESX Server 3.5.0 build-110268'], ['Linux Linux 2.6 Linux'], ['Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'], ['Microsoft <R> Windows <R> 2000 Advanced Server 1.0'], ['Microsoft Windows XP Win2008R2 6.1.7601']]
print(first_decimal_to_tenths(input_list))
