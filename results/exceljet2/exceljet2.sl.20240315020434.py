def get_last_domain_parts(expressions):
    result = []
    for expression in expressions:
        last_dot_index = expression[0].rfind('.')
        if last_dot_index != -1:
            result.append(expression[0][last_dot_index + 1:])
    return result

input_expression = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
output_result = get_last_domain_parts(input_expression)
print(output_result)
