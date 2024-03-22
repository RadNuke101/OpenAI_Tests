# Prompt: add "/n" between the first and second inputted expression, and between the second and third inputted expression
# Input: ['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']
# Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607

def format_address(input_data):
    return '/n'.join(input_data)

# Test cases
print(format_address(['Traci Brown', '1301 Robinson Court', 'Saginaw, MI 48607']))  # Output: Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607
print(format_address(['Mary Hannan', '1195 Amethyst Drive', 'Lansing, MI 48933']))  # Output: Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933
print(format_address(['Linda Thomas', '2479 North Bend Road', 'Allen, KY 41601']))  # Output: Linda Thomas/n2479 North Bend Road/nAllen, KY 41601
Traci Brown/n1301 Robinson Court/nSaginaw, MI 48607
Mary Hannan/n1195 Amethyst Drive/nLansing, MI 48933
Linda Thomas/n2479 North Bend Road/nAllen, KY 41601
