# Solution:
def count_phrase(expression, phrase):
    count = expression.count(phrase)
    return count

print(count_phrase("An example string with _username in it RT _AwesomeUser says _username is awesome", "username"))
print(count_phrase("An example string with _username in it RT _AwesomeUser says _username is awesome", "AwesomeUser"))
print(count_phrase("An _example string with _example in it is awesome _example", "example"))