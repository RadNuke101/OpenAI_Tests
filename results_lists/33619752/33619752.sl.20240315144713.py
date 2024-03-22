def remove_words(input_list):
    output_list = []
    for item in input_list:
        for word in ["Inc", "Company", "Corporation", "Enterprises"]:
            item = item[0].replace(word, "").strip()
        output_list.append(item)
    return output_list

input_list = [['General Electric'], ['General Electric Inc'], ['General Electric Company'], ['Microsoft'], ['Microsoft Corporation'], ['Nintendo'], ['Nintendo Enterprises']]
print(remove_words(input_list))
