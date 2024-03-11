# Define a function that takes in two inputs
def check_expression(expression, second_input):
    # Check if "C0" is in the expression
    if "C0" in expression:
        # If it is, return the entire expression
        return expression
    else:
        # If not, return the second input
        return second_input