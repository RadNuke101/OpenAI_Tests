def generate_emails(input_list):
    output_list = []
    for pair in input_list:
        first_input = pair[0]
        second_input = pair[1]
        new_email = second_input[0] + first_input + '_acme.com'
        output_list.append(new_email)
    return output_list

input_list = [['brown', 'traci'], ['thomas', 'linda'], ['ward', 'jack']]
print(generate_emails(input_list))
