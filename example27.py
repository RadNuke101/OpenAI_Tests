def input_output(expression, column):
    if column == "1":
        return expression.split("-")[0]
    elif column == "2":
        return expression.split("-")[1]