def check_relationship(input_list):
    output = []
    for words in input_list:
        expression = words[0]
        second_word = words[1]
        third_word = words[2]
        fourth_word = words[3]
        
        if second_word in expression and third_word in expression and fourth_word in expression:
            output.append('true')
        else:
            output.append('false')
    
    return output

input_list = [['yellow dog on green grass', 'yellow', 'green', 'dog'], 
              ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'], 
              ['A yellow sun in a green field', 'yellow', 'green', 'dog'], 
              ['yellow neon sign with a green background', 'yellow', 'green', 'dog']]

print(check_relationship(input_list))
