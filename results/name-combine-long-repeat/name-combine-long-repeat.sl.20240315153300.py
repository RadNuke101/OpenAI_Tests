def combine_names(input_list):
    return [' '.join(pair) for pair in input_list]

input_list = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko'], ['Launa', 'Withers'], ['Launa', 'Withers'], ['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Lakenya', 'Edison'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Brendan', 'Hage'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Bradford', 'Lango'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Rudolf', 'Akiyama'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable'], ['Lara', 'Constable'], ['Lara', 'Constable'], ['Madelaine', 'Ghoston'], ['Madelaine', 'Ghoston'], ['Madelaine', 'Ghoston'], ['Salley', 'Hornak'], ['Salley', 'Hornak'], ['Salley', 'Hornak'], ['Micha', 'Junkin'], ['Micha', 'Junkin'], ['Micha', 'Junkin'], ['Teddy', 'Bobo'], ['Teddy', 'Bobo'], ['Teddy', 'Bobo'], ['Coralee', 'Scalia'], ['Coralee', 'Scalia'], ['Coralee', 'Scalia'], ['Jeff', 'Quashie'], ['Jeff', 'Quashie'], ['Jeff', 'Quashie'], ['Vena', 'Babiarz'], ['Vena', 'Babiarz'], ['Vena', 'Babiarz'], ['Karrie', 'Lain'], ['Karrie', 'Lain'], ['Karrie', 'Lain'], ['Tobias', 'Dermody'], ['Tobias', 'Dermody'], ['Tobias', 'Dermody'], ['Celsa', 'Hopkins'], ['Celsa', 'Hopkins'], ['Celsa', 'Hopkins'], ['Kimberley', 'Halpern'], ['Kimberley', 'Halpern'], ['Kimberley', 'Halpern'], ['Phillip', 'Rowden'], ['Phillip', 'Rowden'], ['Phillip', 'Rowden'], ['Elias', 'Neil'], ['Elias', 'Neil'], ['Elias', 'Neil'], ['Lashanda', 'Cortes'], ['Lashanda', 'Cortes'], ['Lashanda', 'Cortes'], ['Mackenzie', 'Spell'], ['Mackenzie', 'Spell'], ['Mackenzie', 'Spell'], ['Kathlyn', 'Eccleston'], ['Kathlyn', 'Eccleston'], ['Kathlyn', 'Eccleston'], ['Georgina', 'Brescia'], ['Georgina', 'Brescia'], ['Georgina', 'Brescia'], ['Beata', 'Miah'], ['Beata', 'Miah'], ['Beata', 'Miah'], ['Desiree', 'Seamons'], ['Desiree', 'Seamons'], ['Desiree', 'Seamons'], ['Jeanice', 'Soderstrom'], ['Jeanice', 'Soderstrom'], ['Jeanice', 'Soderstrom'], ['Mariel', 'Jurgens'], ['Mariel', 'Jurgens'], ['Mariel', 'Jurgens'], ['Alida', 'Bogle'], ['Alida', 'Bogle'], ['Alida', 'Bogle'], ['Jacqualine', 'Olague'], ['Jacqualine', 'Olague'], ['Jacqualine', 'Olague'], ['Joaquin', 'Clasen'], ['Joaquin', 'Clasen'], ['Joaquin', 'Clasen'], ['Samuel', 'Richert'], ['Samuel', 'Richert'], ['Samuel', 'Richert'], ['Malissa', 'Marcus'], ['Malissa', 'Marcus'], ['Malissa', 'Marcus'], ['Alaina', 'Partida'], ['Alaina', 'Partida'], ['Alaina', 'Partida'], ['Trinidad', 'Mulloy'], ['Trinidad', 'Mulloy'], ['Trinidad', 'Mulloy'], ['Carlene', 'Garrard'], ['Carlene', 'Garrard'], ['Carlene', 'Garrard'], ['Melodi', 'Chism'], ['Melodi', 'Chism'], ['Melodi', 'Chism'], ['Bess', 'Chilcott'], ['Bess', 'Chilcott'], ['Bess', 'Chilcott'], ['Chong', 'Aylward'], ['Chong', 'Aylward'], ['Chong', 'Aylward'], ['Jani', 'Ramthun'], ['Jani', 'Ramthun'], ['Jani', 'Ramthun'], ['Jacquiline', 'Heintz'], ['Jacquiline', 'Heintz'], ['Jacquiline', 'Heintz'], ['Hayley', 'Marquess'], ['Hayley', 'Marquess'], ['Hayley', 'Marquess'], ['Andria', 'Spagnoli'], ['Andria', 'Spagnoli'], ['Andria', 'Spagnoli'], ['Irwin', 'Covelli'], ['Irwin', 'Covelli'], ['Irwin', 'Covelli'], ['Gertude', 'Montiel'], ['Gertude', 'Montiel'], ['Gertude', 'Montiel'], ['Stefany', 'Reily'], ['Stefany', 'Reily'], ['Stefany', 'Reily'], ['Rae', 'Mcgaughey'], ['Rae', 'Mcgaughey'], ['Rae', 'Mcgaughey'], ['Cruz', 'Latimore'], ['Cruz', 'Latimore'], ['Cruz', 'Latimore'], ['Maryann', 'Casler'], ['Maryann', 'Casler'], ['Maryann', 'Casler'], ['Annalisa', 'Gregori'], ['Annalisa', 'Gregori'], ['Annalisa', 'Gregori'], ['Jenee', 'Pannell'], ['Jenee', 'Pannell'], ['Jenee', 'Pannell'], ['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable'], ['Madelaine', 'Ghoston'], ['Salley', 'Hornak'], ['Micha', 'Junkin'], ['Teddy', 'Bobo'], ['Coralee', 'Scalia'], ['Jeff', 'Quashie'], ['Vena', 'Babiarz'], ['Karrie', 'Lain'], ['Tobias', 'Dermody'], ['Celsa', 'Hopkins'], ['Kimberley', 'Halpern'], ['Phillip', 'Rowden'], ['Elias', 'Neil'], ['Lashanda', 'Cortes'], ['Mackenzie', 'Spell'], ['Kathlyn', 'Eccleston'], ['Georgina', 'Brescia'], ['Beata', 'Miah'], ['Desiree', 'Seamons'], ['Jeanice', 'Soderstrom'], ['Mariel', 'Jurgens'], ['Alida', 'Bogle'], ['Jacqualine', 'Olague'], ['Joaquin', 'Clasen'], ['Samuel', 'Richert'], ['Malissa', 'Marcus'], ['Alaina', 'Partida'], ['Trinidad', 'Mulloy'], ['Carlene', 'Garrard'], ['Melodi', 'Chism'], ['Bess', 'Chilcott'], ['Chong', 'Aylward'], ['Jani', 'Ramthun'], ['Jacquiline', 'Heintz'], ['Hayley', 'Marquess'], ['Andria', 'Spagnoli'], ['Irwin', 'Covelli'], ['Gertude', 'Montiel'], ['Stefany', 'Reily'], ['Rae', 'Mcgaughey'], ['Cruz', 'Latimore'], ['Maryann', 'Casler'], ['Annalisa', 'Gregori'], ['Jenee', 'Pannell']]

print(combine_names(input_list))
