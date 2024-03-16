def generate_emails(inputs):
    output = []
    for pair in inputs:
        first_letter = pair[1][0]
        email = first_letter + pair[0] + '_acme.com'
        output.append(email)
    return output

inputs = [['brown', 'traci'], ['thomas', 'linda'], ['ward', 'jack']]
print(generate_emails(inputs))
