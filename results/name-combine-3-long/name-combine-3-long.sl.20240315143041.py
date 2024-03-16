def format_names(input_list):
    output_list = []
    for name in input_list:
        formatted_name = name[0][0] + '. ' + name[1]
        output_list.append(formatted_name)
    return output_list

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable'], ['Madelaine', 'Ghoston'], ['Salley', 'Hornak'], ['Micha', 'Junkin'], ['Teddy', 'Bobo'], ['Coralee', 'Scalia'], ['Jeff', 'Quashie'], ['Vena', 'Babiarz'], ['Karrie', 'Lain'], ['Tobias', 'Dermody'], ['Celsa', 'Hopkins'], ['Kimberley', 'Halpern'], ['Phillip', 'Rowden'], ['Elias', 'Neil'], ['Lashanda', 'Cortes'], ['Mackenzie', 'Spell'], ['Kathlyn', 'Eccleston'], ['Georgina', 'Brescia'], ['Beata', 'Miah'], ['Desiree', 'Seamons'], ['Jeanice', 'Soderstrom'], ['Mariel', 'Jurgens'], ['Alida', 'Bogle'], ['Jacqualine', 'Olague'], ['Joaquin', 'Clasen'], ['Samuel', 'Richert'], ['Malissa', 'Marcus'], ['Alaina', 'Partida'], ['Trinidad', 'Mulloy'], ['Carlene', 'Garrard'], ['Melodi', 'Chism'], ['Bess', 'Chilcott'], ['Chong', 'Aylward'], ['Jani', 'Ramthun'], ['Jacquiline', 'Heintz'], ['Hayley', 'Marquess'], ['Andria', 'Spagnoli'], ['Irwin', 'Covelli'], ['Gertude', 'Montiel'], ['Stefany', 'Reily'], ['Rae', 'Mcgaughey'], ['Cruz', 'Latimore'], ['Maryann', 'Casler'], ['Annalisa', 'Gregori'], ['Jenee', 'Pannell']]

print(format_names(input_list))
