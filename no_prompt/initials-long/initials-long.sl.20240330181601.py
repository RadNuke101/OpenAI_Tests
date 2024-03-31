# Start time: 2024-03-30 18:27:12.034973

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., given input as ['Launa Withers'] output is L.W., given input as ['Lakenya Edison'] output is L.E., given input as ['Brendan Hage'] output is B.H., given input as ['Bradford Lango'] output is B.L., given input as ['Rudolf Akiyama'] output is R.A., given input as ['Lara Constable'] output is L.C., given input as ['Madelaine Ghoston'] output is M.G., given input as ['Salley Hornak'] output is S.H., given input as ['Micha Junkin'] output is M.J., given input as ['Teddy Bobo'] output is T.B., given input as ['Coralee Scalia'] output is C.S., given input as ['Jeff Quashie'] output is J.Q., given input as ['Vena Babiarz'] output is V.B., given input as ['Karrie Lain'] output is K.L., given input as ['Tobias Dermody'] output is T.D., given input as ['Celsa Hopkins'] output is C.H., given input as ['Kimberley Halpern'] output is K.H., given input as ['Phillip Rowden'] output is P.R., given input as ['Elias Neil'] output is E.N., given input as ['Lashanda Cortes'] output is L.C., given input as ['Mackenzie Spell'] output is M.S., given input as ['Kathlyn Eccleston'] output is K.E., given input as ['Georgina Brescia'] output is G.B., given input as ['Beata Miah'] output is B.M., given input as ['Desiree Seamons'] output is D.S., given input as ['Jeanice Soderstrom'] output is J.S., given input as ['Mariel Jurgens'] output is M.J., given input as ['Alida Bogle'] output is A.B., given input as ['Jacqualine Olague'] output is J.O., given input as ['Joaquin Clasen'] output is J.C., given input as ['Samuel Richert'] output is S.R., given input as ['Malissa Marcus'] output is M.M., given input as ['Alaina Partida'] output is A.P., given input as ['Trinidad Mulloy'] output is T.M., given input as ['Carlene Garrard'] output is C.G., given input as ['Melodi Chism'] output is M.C., given input as ['Bess Chilcott'] output is B.C., given input as ['Chong Aylward'] output is C.A., given input as ['Jani Ramthun'] output is J.R., given input as ['Jacquiline Heintz'] output is J.H., given input as ['Hayley Marquess'] output is H.M., given input as ['Andria Spagnoli'] output is A.S., given input as ['Irwin Covelli'] output is I.C., given input as ['Gertude Montiel'] output is G.M., given input as ['Stefany Reily'] output is S.R., given input as ['Rae Mcgaughey'] output is R.M., given input as ['Cruz Latimore'] output is C.L., given input as ['Maryann Casler'] output is M.C., given input as ['Annalisa Gregori'] output is A.G., given input as ['Jenee Pannell'] output is J.P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
# Input: 'Nancy FreeHafer', Output: 'N.F.'
# Input: 'Andrew Cencici', Output: 'A.C.'
# Input: 'Jan Kotas', Output: 'J.K.'
# Input: 'Mariya Sergienko', Output: 'M.S.'
# Input: 'Launa Withers', Output: 'L.W.'
# Input: 'Lakenya Edison', Output: 'L.E.'
# Input: 'Brendan Hage', Output: 'B.H.'
# Input: 'Bradford Lango', Output: 'B.L.'
# Input: 'Rudolf Akiyama', Output: 'R.A.'
# Input: 'Lara Constable', Output: 'L.C.'
# Input: 'Madelaine Ghoston', Output: 'M.G.'
# Input: 'Salley Hornak', Output: 'S.H.'
# Input: 'Micha Junkin', Output: 'M.J.'
# Input: 'Teddy Bobo', Output: 'T.B.'
# Input: 'Coralee Scalia', Output: 'C.S.'
# Input: 'Jeff Quashie', Output: 'J.Q.'
# Input: 'Vena Babiarz', Output: 'V.B.'
# Input: 'Karrie Lain', Output: 'K.L.'
# Input: 'Tobias Dermody', Output: 'T.D.'
# Input: 'Celsa Hopkins', Output: 'C.H.'
# Input: 'Kimberley Halpern', Output: 'K.H.'
# Input: 'Phillip Rowden', Output: 'P.R.'
# Input: 'Elias Neil', Output: 'E.N.'
# Input: 'Lashanda Cortes', Output: 'L.C.'
# Input: 'Mackenzie Spell', Output: 'M.S.'
# Input: 'Kathlyn Eccleston', Output: 'K.E.'
# Input: 'Georgina Brescia', Output: 'G.B.'
# Input: 'Beata Miah', Output: 'B.M.'
# Input: 'Desiree Seamons', Output: 'D.S.'
# Input: 'Jeanice Soderstrom', Output: 'J.S.'
# Input: 'Mariel Jurgens', Output: 'M.J.'
# Input: 'Alida Bogle', Output: 'A.B.'
# Input: 'Jacqualine Olague', Output: 'J.O.'
# Input: 'Joaquin Clasen', Output: 'J.C.'
# Input: 'Samuel Richert', Output: 'S.R.'
# Input: 'Malissa Marcus', Output: 'M.M.'
# Input: 'Alaina Partida', Output: 'A.P.'
# Input: 'Trinidad Mulloy', Output: 'T.M.'
# Input: 'Carlene Garrard', Output: 'C.G.'
# Input: 'Melodi Chism', Output: 'M.C.'
# Input: 'Bess Chilcott', Output: 'B.C.'
# Input: 'Chong Aylward', Output: 'C.A.'
# Input: 'Jani Ramthun', Output: 'J.R.'
# Input: 'Jacquiline Heintz', Output: 'J.H.'
# Input: 'Hayley Marquess', Output: 'H.M.'
# Input: 'Andria Spagnoli', Output: 'A.S.'
# Input: 'Irwin Covelli', Output: 'I.C.'
# Input: 'Gertude Montiel', Output: 'G.M.'
# Input: 'Stefany Reily', Output: 'S.R.'
# Input: 'Rae Mcgaughey', Output: 'R.M.'
# Input: 'Cruz Latimore', Output: 'C.L.'
# Input: 'Maryann Casler', Output: 'M.C.'
# Input: 'Annalisa Gregori', Output: 'A.G.'
# Input: 'Jenee Pannell', Output: 'J.P.'

def generate_initials(name):
    try:
        # Split the name into parts
        parts = name.split()
        
        # Get the first letter of the first name and the first letter of the last name
        initials = parts[0][0].upper() + '.' + parts[-1][0].upper() + '.'
        
        return initials
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function with the provided test cases
print(generate_initials('Nancy FreeHafer'))  # Output: N.F.
print(generate_initials('Andrew Cencici'))  # Output: A.C.
print(generate_initials('Jan Kotas'))  # Output: J.K.
print(generate_initials('Mariya Sergienko'))  # Output: M.S.
print(generate_initials('Launa Withers'))  # Output: L.W.
print(generate_initials('Lakenya Edison'))  # Output: L.E.
print(generate_initials('Brendan Hage'))  # Output: B.H.
print(generate_initials('Bradford Lango'))  # Output: B.L.
print(generate_initials('Rudolf Akiyama'))  # Output: R.A.
print(generate_initials('Lara Constable'))  # Output: L.C.
print(generate_initials('Madelaine Ghoston'))  # Output: M.G.
print(generate_initials('Salley Hornak'))  # Output: S.H.
print(generate_initials('Micha Junkin'))  # Output: M.J.
print(generate_initials('Teddy Bobo'))  # Output: T.B.
print(generate_initials('Coralee Scalia'))  # Output: C.S.
print(generate_initials('Jeff Quashie'))  # Output: J.Q.
print(generate_initials('Vena Babiarz'))  # Output: V.B.
print(generate_initials('Karrie Lain'))  # Output: K.L.
print(generate_initials('Tobias Dermody'))  # Output: T.D.
print(generate_initials('Celsa Hopkins'))  # Output: C.H.
print(generate_initials('Kimberley Halpern'))  # Output: K.H.
print(generate_initials('Phillip Rowden'))  # Output: P.R.
print(generate_initials('Elias Neil'))  # Output: E.N.
print(generate_initials('Lashanda Cortes'))  # Output: L.C.
print(generate_initials('Mackenzie Spell'))  # Output: M.S.
print(generate_initials('Kathlyn Eccleston'))  # Output: K.E.
print(generate_initials('Georgina Brescia'))  # Output: G.B.
print(generate_initials('Beata Miah'))  # Output: B.M.
print(generate_initials('Desiree Seamons'))  # Output: D.S.
print(generate_initials('Jeanice Soderstrom'))  # Output: J.S.
print(generate_initials('Mariel Jurgens'))  # Output: M.J.
print(generate_initials('Alida Bogle'))  # Output: A.B.
print(generate_initials('Jacqualine Olague'))  # Output: J.O.
print(generate_initials('Joaquin Clasen'))  # Output: J.C.
print(generate_initials('Samuel Richert'))  # Output: S.R.
print(generate_initials('Malissa Marcus'))  # Output: M.M.
print(generate_initials('Alaina Partida'))  # Output: A.P.
print(generate_initials('Trinidad Mulloy'))  # Output: T.M.
print(generate_initials('Carlene Garrard'))  # Output: C.G.
print(generate_initials('Melodi Chism'))  # Output: M.C.
print(generate_initials('Bess Chilcott'))  # Output: B.C.
print(generate_initials('Chong Aylward'))  # Output: C.A.
print(generate_initials('Jani Ramthun'))  # Output: J.R.
print(generate_initials('Jacquiline Heintz'))  # Output: J.H.
print(generate_initials('Hayley Marquess'))  # Output: H.M.
print(generate_initials('Andria Spagnoli'))  # Output: A.S.
print(generate_initials('Irwin Covelli'))  # Output: I.C.
print(generate_initials('Gertude Montiel'))  # Output: G.M.
print(generate_initials('Stefany Reily'))  # Output: S.R.
print(generate_initials('Rae Mcgaughey'))  # Output: R.M.
print(generate_initials('Cruz Latimore'))  # Output: C.L.
print(generate_initials('Maryann Casler'))  # Output: M.C.
print(generate_initials('Annalisa Gregori'))  # Output: A.G.
print(generate_initials('Jenee Pannell'))  # Output: J.P.

# End time: 2024-03-30 18:27:50.847208
# Elapsed time in seconds: 38.800317542000016