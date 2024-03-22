def generate_emails(input_list):
    output_list = []
    for pair in input_list:
        first_letter = pair[1][0]
        email = first_letter + pair[0] + '_acme.com'
        output_list.append(email)
    return output_list

input_list = [['brown', 'traci'], ['thomas', 'linda'], ['ward', 'jack']]
print(generate_emails(input_list))
