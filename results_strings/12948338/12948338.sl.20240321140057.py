# Prompt: return count of the phrase (second column) in expression (first column)
# Input: 'An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'
# Output: 2
def count_phrase_in_expression(expression, phrase):
    count = expression.count(phrase)
    return count

# Test cases
print(count_phrase_in_expression('An example string with _username in it RT _AwesomeUser says _username is awesome', 'username')) # Output: 2
print(count_phrase_in_expression('An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser')) # Output: 1
print(count_phrase_in_expression('An _example string with _example in it is awesome _example', 'example')) # Output: 3
