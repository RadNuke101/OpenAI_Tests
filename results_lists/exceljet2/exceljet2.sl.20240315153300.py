def get_last_domains(expressions):
    return [expression[0].split('.')[-1] for expression in expressions]

# Test the function with the provided input
input_expr = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
output = get_last_domains(input_expr)
print(output)
