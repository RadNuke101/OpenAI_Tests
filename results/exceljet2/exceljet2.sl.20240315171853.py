def return_last_domain(input_expression):
    output = []
    for expression in input_expression:
        last_dot_index = expression[0].rfind('.')
        if last_dot_index != -1:
            output.append(expression[0][last_dot_index+1:])
    return output

input_expression = [['www.domain.com'], ['mail.net'], ['www.amaon.co.uk']]
print(return_last_domain(input_expression))
