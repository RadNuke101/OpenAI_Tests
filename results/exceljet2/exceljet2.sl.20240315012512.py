def return_last_part(expressions):
    result = []
    for expression in expressions:
        last_dot_index = expression[0].rfind('.')
        result.append(expression[0][last_dot_index + 1:])
    return result

input_expression = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
output_result = return_last_part(input_expression)
print(output_result)
