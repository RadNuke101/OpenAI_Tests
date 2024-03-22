def get_initials(input_str):
    words = input_str.split()
    initials = words[0][0].upper() + '.' + words[1][0].upper() + '.'
    return initials

# Prompt: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period
# Input: ['Nancy FreeHafer']
# Output: N.F.

# Test cases
print(get_initials('Nancy FreeHafer'))  # Output: N.F.
print(get_initials('Andrew Cencici'))  # Output: A.C.
print(get_initials('Jan Kotas'))  # Output: J.K.
print(get_initials('Mariya Sergienko'))  # Output: M.S.
print(get_initials('Launa Withers'))  # Output: L.W.
print(get_initials('Lakenya Edison'))  # Output: L.E.
print(get_initials('Brendan Hage'))  # Output: B.H.
print(get_initials('Bradford Lango'))  # Output: B.L.
print(get_initials('Rudolf Akiyama'))  # Output: R.A.
print(get_initials('Lara Constable'))  # Output: L.C.
print(get_initials('Madelaine Ghoston'))  # Output: M.G.
print(get_initials('Salley Hornak'))  # Output: S.H.
print(get_initials('Micha Junkin'))  # Output: M.J.
print(get_initials('Teddy Bobo'))  # Output: T.B.
print(get_initials('Coralee Scalia'))  # Output: C.S.
print(get_initials('Jeff Quashie'))  # Output: J.Q.
print(get_initials('Vena Babiarz'))  # Output: V.B.
print(get_initials('Karrie Lain'))  # Output: K.L.
print(get_initials('Tobias Dermody'))  # Output: T.D.
print(get_initials('Celsa Hopkins'))  # Output: C.H.
print(get_initials('Kimberley Halpern'))  # Output: K.H.
print(get_initials('Phillip Rowden'))  # Output: P.R.
print(get_initials('Elias Neil'))  # Output: E.N.
print(get_initials('Lashanda Cortes'))  # Output: L.C.
print(get_initials('Mackenzie Spell'))  # Output: M.S.
print(get_initials('Kathlyn Eccleston'))  # Output: K.E.
print(get_initials('Georgina Brescia'))  # Output: G.B.
print(get_initials('Beata Miah'))  # Output: B.M.
print(get_initials('Desiree Seamons'))  # Output: D.S.
print(get_initials('Jeanice Soderstrom'))  # Output: J.S.
print(get_initials('Mariel Jurgens'))  # Output: M.J.
print(get_initials('Alida Bogle'))  # Output: A.B.
print(get_initials('Jacqualine Olague'))  # Output: J.O.
print(get_initials('Joaquin Clasen'))  # Output: J.C.
print(get_initials('Samuel Richert'))  # Output: S.R.
print(get_initials('Malissa Marcus'))  # Output: M.M.
print(get_initials('Alaina Partida'))  # Output: A.P.
print(get_initials('Trinidad Mulloy'))  # Output: T.M.
print(get_initials('Carlene Garrard'))  # Output: C.G.
print(get_initials('Melodi Chism'))  # Output: M.C.
print(get_initials('Bess Chilcott'))  # Output: B.C.
print(get_initials('Chong Aylward'))  # Output: C.A.
print(get_initials('Jani Ramthun'))  # Output: J.R.
print(get_initials('Jacquiline Heintz'))  # Output: J.H.
print(get_initials('Hayley Marquess'))  # Output: H.M.
print(get_initials('Andria Spagnoli'))  # Output: A.S.
print(get_initials('Irwin Covelli'))  # Output: I.C.
print(get_initials('Gertude Montiel'))  # Output: G.M.
print(get_initials('Stefany Reily'))  # Output: S.R.
print(get_initials('Rae Mcgaughey'))  # Output: R.M.
print(get_initials('Cruz Latimore'))  # Output: C.L.
print(get_initials('Maryann Casler'))  # Output: M.C.
print(get_initials('Annalisa Gregori'))  # Output: A.G.
print(get_initials('Jenee Pannell'))  # Output: J.P.
