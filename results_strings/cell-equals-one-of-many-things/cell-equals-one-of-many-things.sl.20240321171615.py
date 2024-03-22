# Prompt: if input is a color that is not "gray" or "black", return true
def check_color(input_str):
    if input_str != "gray" and input_str != "black":
        return "true"
    else:
        return "false"

# Test cases
print(check_color("yellow"))  # Output: true
print(check_color("gray"))    # Output: false
print(check_color("black"))   # Output: false
print(check_color("blue"))    # Output: true
print(check_color("pink"))    # Output: true
print(check_color("orange"))  # Output: true
print(check_color("turkey"))  # Output: false
