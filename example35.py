# Python program with function that follows the prompt and returns the outputs when given the inputs

def check_inputs(expression, word1, word2, word3):
    # check if any of the words are in the expression
    if word1 in expression or word2 in expression or word3 in expression:
        return True
    else:
        return False