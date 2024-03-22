def generate_emails(inputs):
    outputs = []
    for input_pair in inputs:
        first_letter = input_pair[1][0]
        email = first_letter + input_pair[0] + '_acme.com'
        outputs.append(email)
    return outputs

inputs = [['brown', 'traci'], ['thomas', 'linda'], ['ward', 'jack']]
print(generate_emails(inputs))
