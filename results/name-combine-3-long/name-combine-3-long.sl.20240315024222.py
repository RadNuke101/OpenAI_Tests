def format_names(names):
    result = []
    for name in names:
        first_letter = name[0][0]
        formatted_name = f"{first_letter}. {name[1]}"
        result.append(formatted_name)
    return result

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable'], ['Madelaine', 'Ghoston'], ['Salley', 'Hornak'], ['Micha', 'Junkin'], ['Teddy', 'Bobo'], ['Coralee', 'Scalia'], ['Jeff', 'Quashie'], ['Vena', 'Babiarz'], ['Karrie', 'Lain'], ['Tobias', 'Dermody'], ['Celsa', 'Hopkins'], ['Kimberley', 'Halpern'], ['Phillip', 'Rowden'], ['Elias', 'Neil'], ['Lashanda', 'Cortes'], ['Mackenzie', 'Spell'], ['Kathlyn', 'Eccleston'], ['Georgina', 'Brescia'], ['Beata', 'Miah'], ['Desiree', 'Seamons'], ['Jeanice', 'Soderstrom'], ['Mariel', 'Jurgens'], ['Alida', 'Bogle'], ['Jacqualine', 'Olague'], ['Joaquin', 'Clasen'], ['Samuel', 'Richert'], ['Malissa', 'Marcus'], ['Alaina', 'Partida'], ['Trinidad', 'Mulloy'], ['Carlene', 'Garrard'], ['Melodi', 'Chism'], ['Bess', 'Chilcott'], ['Chong', 'Aylward'], ['Jani', 'Ramthun'], ['Jacquiline', 'Heintz'], ['Hayley', 'Marquess'], ['Andria', 'Spagnoli'], ['Irwin', 'Covelli'], ['Gertude', 'Montiel'], ['Stefany', 'Reily'], ['Rae', 'Mcgaughey'], ['Cruz', 'Latimore'], ['Maryann', 'Casler'], ['Annalisa', 'Gregori'], ['Jenee', 'Pannell']]
output_data = ['L. Withers', 'L. Edison', 'B. Hage', 'B. Lango', 'R. Akiyama', 'L. Constable', 'M. Ghoston', 'S. Hornak', 'M. Junkin', 'T. Bobo', 'C. Scalia', 'J. Quashie', 'V. Babiarz', 'K. Lain', 'T. Dermody', 'C. Hopkins', 'K. Halpern', 'P. Rowden', 'E. Neil', 'L. Cortes', 'M. Spell', 'K. Eccleston', 'G. Brescia', 'B. Miah', 'D. Seamons', 'J. Soderstrom', 'M. Jurgens', 'A. Bogle', 'J. Olague', 'J. Clasen', 'S. Richert', 'M. Marcus', 'A. Partida', 'T. Mulloy', 'C. Garrard', 'M. Chism', 'B. Chilcott', 'C. Aylward', 'J. Ramthun', 'J. Heintz', 'H. Marquess', 'A. Spagnoli', 'I. Covelli', 'G. Montiel', 'S. Reily', 'R. Mcgaughey', 'C. Latimore', 'M. Casler', 'A. Gregori', 'J. Pannell']

print(format_names(input_data) == output_data)
