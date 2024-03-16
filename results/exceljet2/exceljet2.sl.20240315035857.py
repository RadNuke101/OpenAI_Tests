def return_last_parts(expressions):
    result = []
    for expression in expressions:
        last_part = expression[0].split('.')[-1]
        result.append(last_part)
    return result

input_expression = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
output = return_last_parts(input_expression)
print(output)
