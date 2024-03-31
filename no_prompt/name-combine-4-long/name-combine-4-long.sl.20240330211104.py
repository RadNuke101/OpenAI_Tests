# Start time: 2024-03-30 21:14:55.083840

# Content: Given that given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., given input as ['Lara', 'Constable'] output is Constable, L., given input as ['Madelaine', 'Ghoston'] output is Ghoston, M., given input as ['Salley', 'Hornak'] output is Hornak, S., given input as ['Micha', 'Junkin'] output is Junkin, M., given input as ['Teddy', 'Bobo'] output is Bobo, T., given input as ['Coralee', 'Scalia'] output is Scalia, C., given input as ['Jeff', 'Quashie'] output is Quashie, J., given input as ['Vena', 'Babiarz'] output is Babiarz, V., given input as ['Karrie', 'Lain'] output is Lain, K., given input as ['Tobias', 'Dermody'] output is Dermody, T., given input as ['Celsa', 'Hopkins'] output is Hopkins, C., given input as ['Kimberley', 'Halpern'] output is Halpern, K., given input as ['Phillip', 'Rowden'] output is Rowden, P., given input as ['Elias', 'Neil'] output is Neil, E., given input as ['Lashanda', 'Cortes'] output is Cortes, L., given input as ['Mackenzie', 'Spell'] output is Spell, M., given input as ['Kathlyn', 'Eccleston'] output is Eccleston, K., given input as ['Georgina', 'Brescia'] output is Brescia, G., given input as ['Beata', 'Miah'] output is Miah, B., given input as ['Desiree', 'Seamons'] output is Seamons, D., given input as ['Jeanice', 'Soderstrom'] output is Soderstrom, J., given input as ['Mariel', 'Jurgens'] output is Jurgens, M., given input as ['Alida', 'Bogle'] output is Bogle, A., given input as ['Jacqualine', 'Olague'] output is Olague, J., given input as ['Joaquin', 'Clasen'] output is Clasen, J., given input as ['Samuel', 'Richert'] output is Richert, S., given input as ['Malissa', 'Marcus'] output is Marcus, M., given input as ['Alaina', 'Partida'] output is Partida, A., given input as ['Trinidad', 'Mulloy'] output is Mulloy, T., given input as ['Carlene', 'Garrard'] output is Garrard, C., given input as ['Melodi', 'Chism'] output is Chism, M., given input as ['Bess', 'Chilcott'] output is Chilcott, B., given input as ['Chong', 'Aylward'] output is Aylward, C., given input as ['Jani', 'Ramthun'] output is Ramthun, J., given input as ['Jacquiline', 'Heintz'] output is Heintz, J., given input as ['Hayley', 'Marquess'] output is Marquess, H., given input as ['Andria', 'Spagnoli'] output is Spagnoli, A., given input as ['Irwin', 'Covelli'] output is Covelli, I., given input as ['Gertude', 'Montiel'] output is Montiel, G., given input as ['Stefany', 'Reily'] output is Reily, S., given input as ['Rae', 'Mcgaughey'] output is Mcgaughey, R., given input as ['Cruz', 'Latimore'] output is Latimore, C., given input as ['Maryann', 'Casler'] output is Casler, M., given input as ['Annalisa', 'Gregori'] output is Gregori, A., given input as ['Jenee', 'Pannell'] output is Pannell, J., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        # Input: 'Launa, Withers' Output: 'Withers, L.'
        last_name, first_name = name.split(', ')
        return f"{last_name}, {first_name[0]}."
    except ValueError:
        print("Invalid input format. Please provide input in the format 'Lastname, Firstname'.")

# Test cases
print(format_name('Launa, Withers'))
print(format_name('Lakenya, Edison'))
print(format_name('Brendan, Hage'))
print(format_name('Bradford, Lango'))
print(format_name('Rudolf, Akiyama'))
print(format_name('Lara, Constable'))
print(format_name('Madelaine, Ghoston'))
print(format_name('Salley, Hornak'))
print(format_name('Micha, Junkin'))
print(format_name('Teddy, Bobo'))
print(format_name('Coralee, Scalia'))
print(format_name('Jeff, Quashie'))
print(format_name('Vena, Babiarz'))
print(format_name('Karrie, Lain'))
print(format_name('Tobias, Dermody'))
print(format_name('Celsa, Hopkins'))
print(format_name('Kimberley, Halpern'))
print(format_name('Phillip, Rowden'))
print(format_name('Elias, Neil'))
print(format_name('Lashanda, Cortes'))
print(format_name('Mackenzie, Spell'))
print(format_name('Kathlyn, Eccleston'))
print(format_name('Georgina, Brescia'))
print(format_name('Beata, Miah'))
print(format_name('Desiree, Seamons'))
print(format_name('Jeanice, Soderstrom'))
print(format_name('Mariel, Jurgens'))
print(format_name('Alida, Bogle'))
print(format_name('Jacqualine, Olague'))
print(format_name('Joaquin, Clasen'))
print(format_name('Samuel, Richert'))
print(format_name('Malissa, Marcus'))
print(format_name('Alaina, Partida'))
print(format_name('Trinidad, Mulloy'))
print(format_name('Carlene, Garrard'))
print(format_name('Melodi, Chism'))
print(format_name('Bess, Chilcott'))
print(format_name('Chong, Aylward'))
print(format_name('Jani, Ramthun'))
print(format_name('Jacquiline, Heintz'))
print(format_name('Hayley, Marquess'))
print(format_name('Andria, Spagnoli'))
print(format_name('Irwin, Covelli'))
print(format_name('Gertude, Montiel'))
print(format_name('Stefany, Reily'))
print(format_name('Rae, Mcgaughey'))
print(format_name('Cruz, Latimore'))
print(format_name('Maryann, Casler'))
print(format_name('Annalisa, Gregori'))
print(format_name('Jenee, Pannell'))

# End time: 2024-03-30 21:15:09.019988
# Elapsed time in seconds: 13.935837111001092