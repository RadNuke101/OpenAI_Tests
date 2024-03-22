# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input

def format_inputs(*args):
    result = ""
    for arg in args:
        if arg != "":
            result += arg + ", "
    return result.rstrip(", ")

# Test cases
print(format_inputs('figs', '', 'apples'))  # Output: figs, apples
print(format_inputs('mangos', 'kiwis', 'grapes'))  # Output: mangos, kiwis, grapes
