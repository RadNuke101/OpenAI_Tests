def get_letter_at_position(expression, position):
    return expression[position-1]

for i in range(5):
    input_1 = input()
    input_2 = int(input())
    output = get_letter_at_position(input_1, input_2)
    print(output)