def generate_emails(inputs):
    outputs = []
    for input_pair in inputs:
        first_input = input_pair[0]
        second_input = input_pair[1]
        email = second_input[0] + first_input + '_acme.com'
        outputs.append(email)
    return outputs

inputs = [['brown', 'traci'], ['thomas', 'linda'], ['ward', 'jack']]
print(generate_emails(inputs))
