
def first_word(input):
    if "1" in input:
        return input.split(",")[0] + " apple"
    elif "2" in input:
        return input.split(",")[0] + " bananas"
    elif "3" in input:
        return input.split(",")[0] + " strawberries"
    elif "4" in input:
        return input.split(",")[0] + " oranges"