def format_names(input):
    first_name = input[0]
    last_name = input[1]
    output = last_name + ', ' + first_name[0] + '.'
    return output

# Input: ['Launa', 'Withers']
# Output: Withers, L.
# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period

# Test cases
print(format_names(['Launa', 'Withers']))  # Output: Withers, L.
print(format_names(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_names(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_names(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_names(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
print(format_names(['Lara', 'Constable']))  # Output: Constable, L.
print(format_names(['Madelaine', 'Ghoston']))  # Output: Ghoston, M.
print(format_names(['Salley', 'Hornak']))  # Output: Hornak, S.
print(format_names(['Micha', 'Junkin']))  # Output: Junkin, M.
print(format_names(['Teddy', 'Bobo']))  # Output: Bobo, T.
print(format_names(['Coralee', 'Scalia']))  # Output: Scalia, C.
print(format_names(['Jeff', 'Quashie']))  # Output: Quashie, J.
print(format_names(['Vena', 'Babiarz']))  # Output: Babiarz, V.
print(format_names(['Karrie', 'Lain']))  # Output: Lain, K.
print(format_names(['Tobias', 'Dermody']))  # Output: Dermody, T.
print(format_names(['Celsa', 'Hopkins']))  # Output: Hopkins, C.
print(format_names(['Kimberley', 'Halpern']))  # Output: Halpern, K.
print(format_names(['Phillip', 'Rowden']))  # Output: Rowden, P.
print(format_names(['Elias', 'Neil']))  # Output: Neil, E.
print(format_names(['Lashanda', 'Cortes']))  # Output: Cortes, L.
print(format_names(['Mackenzie', 'Spell']))  # Output: Spell, M.
print(format_names(['Kathlyn', 'Eccleston']))  # Output: Eccleston, K.
print(format_names(['Georgina', 'Brescia']))  # Output: Brescia, G.
print(format_names(['Beata', 'Miah']))  # Output: Miah, B.
print(format_names(['Desiree', 'Seamons']))  # Output: Seamons, D.
print(format_names(['Jeanice', 'Soderstrom']))  # Output: Soderstrom, J.
print(format_names(['Mariel', 'Jurgens']))  # Output: Jurgens, M.
print(format_names(['Alida', 'Bogle']))  # Output: Bogle, A.
print(format_names(['Jacqualine', 'Olague']))  # Output: Olague, J.
print(format_names(['Joaquin', 'Clasen']))  # Output: Clasen, J.
print(format_names(['Samuel', 'Richert']))  # Output: Richert, S.
print(format_names(['Malissa', 'Marcus']))  # Output: Marcus, M.
print(format_names(['Alaina', 'Partida']))  # Output: Partida, A.
print(format_names(['Trinidad', 'Mulloy']))  # Output: Mulloy, T.
print(format_names(['Carlene', 'Garrard']))  # Output: Garrard, C.
print(format_names(['Melodi', 'Chism']))  # Output: Chism, M.
print(format_names(['Bess', 'Chilcott']))  # Output: Chilcott, B.
print(format_names(['Chong', 'Aylward']))  # Output: Aylward, C.
print(format_names(['Jani', 'Ramthun']))  # Output: Ramthun, J.
print(format_names(['Jacquiline', 'Heintz']))  # Output: Heintz, J.
print(format_names(['Hayley', 'Marquess']))  # Output: Marquess, H.
print(format_names(['Andria', 'Spagnoli']))  # Output: Spagnoli, A.
print(format_names(['Irwin', 'Covelli']))  # Output: Covelli, I.
print(format_names(['Gertude', 'Montiel']))  # Output: Montiel, G.
print(format_names(['Stefany', 'Reily']))  # Output: Reily, S.
print(format_names(['Rae', 'Mcgaughey']))  # Output: Mcgaughey, R.
print(format_names(['Cruz', 'Latimore']))  # Output: Latimore, C.
print(format_names(['Maryann', 'Casler']))  # Output: Casler, M.
print(format_names(['Annalisa', 'Gregori']))  # Output: Gregori, A.
print(format_names(['Jenee', 'Pannell']))  # Output: Pannell, J.
