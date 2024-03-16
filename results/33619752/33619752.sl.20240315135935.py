def remove_words(input_list):
    output_list = []
    for item in input_list:
        name = item[0].replace(" Inc", "").replace(" Company", "").replace(" Corporation", "").replace(" Enterprises", "")
        output_list.append(name)
    return output_list

input_list = [['General Electric'], ['General Electric Inc'], ['General Electric Company'], ['Microsoft'], ['Microsoft Corporation'], ['Nintendo'], ['Nintendo Enterprises']]
print(remove_words(input_list))
