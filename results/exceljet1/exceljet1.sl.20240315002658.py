def return_after_underscore(lst):
    result = []
    for item in lst:
        second_input = item[1]
        after_underscore = second_input.split('_')[-1]
        result.append(after_underscore)
    return result

input_data = [['ann chang', 'achang_maaker.com'], ['bobby smith', 'bobt_sphynx.uk.co'], ['art lennox', 'art.lennox_svxn.com'], ['smith bagshaw', 'smith_bbbbb.com']]
output = return_after_underscore(input_data)
print(output)
