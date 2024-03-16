# Define function
def return_expression(expression):
    # Split input by "=" sign
    inputs = expression.split("=")
    # Return expression after "=" sign
    return inputs[1]