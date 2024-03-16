def format_names(names):
    result = []
    for name in names:
        result.append(name[0] + ' ' + name[1][0] + '.')
    return result

input_data = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko'], ['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable'], ['Madelaine', 'Ghoston'], ['Salley', 'Hornak'], ['Micha', 'Junkin'], ['Teddy', 'Bobo'], ['Coralee', 'Scalia'], ['Jeff', 'Quashie'], ['Vena', 'Babiarz'], ['Karrie', 'Lain'], ['Tobias', 'Dermody'], ['Celsa', 'Hopkins'], ['Kimberley', 'Halpern'], ['Phillip', 'Rowden'], ['Elias', 'Neil'], ['Lashanda', 'Cortes'], ['Mackenzie', 'Spell'], ['Kathlyn', 'Eccleston'], ['Georgina', 'Brescia'], ['Beata', 'Miah'], ['Desiree', 'Seamons'], ['Jeanice', 'Soderstrom'], ['Mariel', 'Jurgens'], ['Alida', 'Bogle'], ['Jacqualine', 'Olague'], ['Joaquin', 'Clasen'], ['Samuel', 'Richert'], ['Malissa', 'Marcus'], ['Alaina', 'Partida'], ['Trinidad', 'Mulloy'], ['Carlene', 'Garrard'], ['Melodi', 'Chism'], ['Bess', 'Chilcott'], ['Chong', 'Aylward'], ['Jani', 'Ramthun'], ['Jacquiline', 'Heintz'], ['Hayley', 'Marquess'], ['Andria', 'Spagnoli'], ['Irwin', 'Covelli'], ['Gertude', 'Montiel'], ['Stefany', 'Reily'], ['Rae', 'Mcgaughey'], ['Cruz', 'Latimore'], ['Maryann', 'Casler'], ['Annalisa', 'Gregori'], ['Jenee', 'Pannell']]

output_data = ['Nancy F.', 'Andrew C.', 'Jan K.', 'Mariya S.', 'Launa W.', 'Lakenya E.', 'Brendan H.', 'Bradford L.', 'Rudolf A.', 'Lara C.', 'Madelaine G.', 'Salley H.', 'Micha J.', 'Teddy B.', 'Coralee S.', 'Jeff Q.', 'Vena B.', 'Karrie L.', 'Tobias D.', 'Celsa H.', 'Kimberley H.', 'Phillip R.', 'Elias N.', 'Lashanda C.', 'Mackenzie S.', 'Kathlyn E.', 'Georgina B.', 'Beata M.', 'Desiree S.', 'Jeanice S.', 'Mariel J.', 'Alida B.', 'Jacqualine O.', 'Joaquin C.', 'Samuel R.', 'Malissa M.', 'Alaina P.', 'Trinidad M.', 'Carlene G.', 'Melodi C.', 'Bess C.', 'Chong A.', 'Jani R.', 'Jacquiline H.', 'Hayley M.', 'Andria S.', 'Irwin C.', 'Gertude M.', 'Stefany R.', 'Rae M.', 'Cruz L.', 'Maryann C.', 'Annalisa G.', 'Jenee P.']

print(format_names(input_data) == output_data)
