def format_names(input):
    output = []
    for names in input:
        output.append(names[1] + ', ' + names[0][0] + '.')
    return output

input = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama']]
print(format_names(input))
