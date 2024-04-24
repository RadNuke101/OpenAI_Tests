# Start time: 2024-04-10 17:55:27.254897

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., input as ['Launa Withers'] output is L.W., input as ['Lakenya Edison'] output is L.E., input as ['Brendan Hage'] output is B.H., input as ['Bradford Lango'] output is B.L., input as ['Rudolf Akiyama'] output is R.A., input as ['Lara Constable'] output is L.C., input as ['Madelaine Ghoston'] output is M.G., input as ['Salley Hornak'] output is S.H., input as ['Micha Junkin'] output is M.J., input as ['Teddy Bobo'] output is T.B., input as ['Coralee Scalia'] output is C.S., input as ['Jeff Quashie'] output is J.Q., input as ['Vena Babiarz'] output is V.B., input as ['Karrie Lain'] output is K.L., input as ['Tobias Dermody'] output is T.D., input as ['Celsa Hopkins'] output is C.H., input as ['Kimberley Halpern'] output is K.H., input as ['Phillip Rowden'] output is P.R., input as ['Elias Neil'] output is E.N., input as ['Lashanda Cortes'] output is L.C., input as ['Mackenzie Spell'] output is M.S., input as ['Kathlyn Eccleston'] output is K.E., input as ['Georgina Brescia'] output is G.B., input as ['Beata Miah'] output is B.M., input as ['Desiree Seamons'] output is D.S., input as ['Jeanice Soderstrom'] output is J.S., input as ['Mariel Jurgens'] output is M.J., input as ['Alida Bogle'] output is A.B., input as ['Jacqualine Olague'] output is J.O., input as ['Joaquin Clasen'] output is J.C., input as ['Samuel Richert'] output is S.R., input as ['Malissa Marcus'] output is M.M., input as ['Alaina Partida'] output is A.P., input as ['Trinidad Mulloy'] output is T.M., input as ['Carlene Garrard'] output is C.G., input as ['Melodi Chism'] output is M.C., input as ['Bess Chilcott'] output is B.C., input as ['Chong Aylward'] output is C.A., input as ['Jani Ramthun'] output is J.R., input as ['Jacquiline Heintz'] output is J.H., input as ['Hayley Marquess'] output is H.M., input as ['Andria Spagnoli'] output is A.S., input as ['Irwin Covelli'] output is I.C., input as ['Gertude Montiel'] output is G.M., input as ['Stefany Reily'] output is S.R., input as ['Rae Mcgaughey'] output is R.M., input as ['Cruz Latimore'] output is C.L., input as ['Maryann Casler'] output is M.C., input as ['Annalisa Gregori'] output is A.G., input as ['Jenee Pannell'] output is J.P., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name):
    try:
        # Split the input name into first name and last name
        first_name, last_name = name.split()
        
        # Get the first letter of the first name and last name
        initials = f"{first_name[0]}.{last_name[0]}."
        
        return initials
    except ValueError:
        return "Invalid input format. Please provide a full name with a space in between."

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function('Launa Withers'))
print(generated_function('Lakenya Edison'))
print(generated_function('Brendan Hage'))
print(generated_function('Bradford Lango'))
print(generated_function('Rudolf Akiyama'))
print(generated_function('Lara Constable'))
print(generated_function('Madelaine Ghoston'))
print(generated_function('Salley Hornak'))
print(generated_function('Micha Junkin'))
print(generated_function('Teddy Bobo'))
print(generated_function('Coralee Scalia'))
print(generated_function('Jeff Quashie'))
print(generated_function('Vena Babiarz'))
print(generated_function('Karrie Lain'))
print(generated_function('Tobias Dermody'))
print(generated_function('Celsa Hopkins'))
print(generated_function('Kimberley Halpern'))
print(generated_function('Phillip Rowden'))
print(generated_function('Elias Neil'))
print(generated_function('Lashanda Cortes'))
print(generated_function('Mackenzie Spell'))
print(generated_function('Kathlyn Eccleston'))
print(generated_function('Georgina Brescia'))
print(generated_function('Beata Miah'))
print(generated_function('Desiree Seamons'))
print(generated_function('Jeanice Soderstrom'))
print(generated_function('Mariel Jurgens'))
print(generated_function('Alida Bogle'))
print(generated_function('Jacqualine Olague'))
print(generated_function('Joaquin Clasen'))
print(generated_function('Samuel Richert'))
print(generated_function('Malissa Marcus'))
print(generated_function('Alaina Partida'))
print(generated_function('Trinidad Mulloy'))
print(generated_function('Carlene Garrard'))
print(generated_function('Melodi Chism'))
print(generated_function('Bess Chilcott'))
print(generated_function('Chong Aylward'))
print(generated_function('Jani Ramthun'))
print(generated_function('Jacquiline Heintz'))
print(generated_function('Hayley Marquess'))
print(generated_function('Andria Spagnoli'))
print(generated_function('Irwin Covelli'))
print(generated_function('Gertude Montiel'))
print(generated_function('Stefany Reily'))
print(generated_function('Rae Mcgaughey'))
print(generated_function('Cruz Latimore'))
print(generated_function('Maryann Casler'))
print(generated_function('Annalisa Gregori'))
print(generated_function('Jenee Pannell'))
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.
print(generated_function("Launa Withers"))  ## Output: L.W.
print(generated_function("Lakenya Edison"))  ## Output: L.E.
print(generated_function("Brendan Hage"))  ## Output: B.H.
print(generated_function("Bradford Lango"))  ## Output: B.L.
print(generated_function("Rudolf Akiyama"))  ## Output: R.A.
print(generated_function("Lara Constable"))  ## Output: L.C.
print(generated_function("Madelaine Ghoston"))  ## Output: M.G.
print(generated_function("Salley Hornak"))  ## Output: S.H.
print(generated_function("Micha Junkin"))  ## Output: M.J.
print(generated_function("Teddy Bobo"))  ## Output: T.B.
print(generated_function("Coralee Scalia"))  ## Output: C.S.
print(generated_function("Jeff Quashie"))  ## Output: J.Q.
print(generated_function("Vena Babiarz"))  ## Output: V.B.
print(generated_function("Karrie Lain"))  ## Output: K.L.
print(generated_function("Tobias Dermody"))  ## Output: T.D.
print(generated_function("Celsa Hopkins"))  ## Output: C.H.
print(generated_function("Kimberley Halpern"))  ## Output: K.H.
print(generated_function("Phillip Rowden"))  ## Output: P.R.
print(generated_function("Elias Neil"))  ## Output: E.N.
print(generated_function("Lashanda Cortes"))  ## Output: L.C.
print(generated_function("Mackenzie Spell"))  ## Output: M.S.
print(generated_function("Kathlyn Eccleston"))  ## Output: K.E.
print(generated_function("Georgina Brescia"))  ## Output: G.B.
print(generated_function("Beata Miah"))  ## Output: B.M.
print(generated_function("Desiree Seamons"))  ## Output: D.S.
print(generated_function("Jeanice Soderstrom"))  ## Output: J.S.
print(generated_function("Mariel Jurgens"))  ## Output: M.J.
print(generated_function("Alida Bogle"))  ## Output: A.B.
print(generated_function("Jacqualine Olague"))  ## Output: J.O.
print(generated_function("Joaquin Clasen"))  ## Output: J.C.
print(generated_function("Samuel Richert"))  ## Output: S.R.
print(generated_function("Malissa Marcus"))  ## Output: M.M.
print(generated_function("Alaina Partida"))  ## Output: A.P.
print(generated_function("Trinidad Mulloy"))  ## Output: T.M.
print(generated_function("Carlene Garrard"))  ## Output: C.G.
print(generated_function("Melodi Chism"))  ## Output: M.C.
print(generated_function("Bess Chilcott"))  ## Output: B.C.
print(generated_function("Chong Aylward"))  ## Output: C.A.
print(generated_function("Jani Ramthun"))  ## Output: J.R.
print(generated_function("Jacquiline Heintz"))  ## Output: J.H.
print(generated_function("Hayley Marquess"))  ## Output: H.M.
print(generated_function("Andria Spagnoli"))  ## Output: A.S.
print(generated_function("Irwin Covelli"))  ## Output: I.C.
print(generated_function("Gertude Montiel"))  ## Output: G.M.
print(generated_function("Stefany Reily"))  ## Output: S.R.
print(generated_function("Rae Mcgaughey"))  ## Output: R.M.
print(generated_function("Cruz Latimore"))  ## Output: C.L.
print(generated_function("Maryann Casler"))  ## Output: M.C.
print(generated_function("Annalisa Gregori"))  ## Output: A.G.
print(generated_function("Jenee Pannell"))  ## Output: J.P.

# End time: 2024-04-10 17:55:37.231501
# Elapsed time in seconds: 9.976339374999952


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.
print(generated_function("Launa Withers"))  ## Output: L.W.
print(generated_function("Lakenya Edison"))  ## Output: L.E.
print(generated_function("Brendan Hage"))  ## Output: B.H.
print(generated_function("Bradford Lango"))  ## Output: B.L.
print(generated_function("Rudolf Akiyama"))  ## Output: R.A.
print(generated_function("Lara Constable"))  ## Output: L.C.
print(generated_function("Madelaine Ghoston"))  ## Output: M.G.
print(generated_function("Salley Hornak"))  ## Output: S.H.
print(generated_function("Micha Junkin"))  ## Output: M.J.
print(generated_function("Teddy Bobo"))  ## Output: T.B.
print(generated_function("Coralee Scalia"))  ## Output: C.S.
print(generated_function("Jeff Quashie"))  ## Output: J.Q.
print(generated_function("Vena Babiarz"))  ## Output: V.B.
print(generated_function("Karrie Lain"))  ## Output: K.L.
print(generated_function("Tobias Dermody"))  ## Output: T.D.
print(generated_function("Celsa Hopkins"))  ## Output: C.H.
print(generated_function("Kimberley Halpern"))  ## Output: K.H.
print(generated_function("Phillip Rowden"))  ## Output: P.R.
print(generated_function("Elias Neil"))  ## Output: E.N.
print(generated_function("Lashanda Cortes"))  ## Output: L.C.
print(generated_function("Mackenzie Spell"))  ## Output: M.S.
print(generated_function("Kathlyn Eccleston"))  ## Output: K.E.
print(generated_function("Georgina Brescia"))  ## Output: G.B.
print(generated_function("Beata Miah"))  ## Output: B.M.
print(generated_function("Desiree Seamons"))  ## Output: D.S.
print(generated_function("Jeanice Soderstrom"))  ## Output: J.S.
print(generated_function("Mariel Jurgens"))  ## Output: M.J.
print(generated_function("Alida Bogle"))  ## Output: A.B.
print(generated_function("Jacqualine Olague"))  ## Output: J.O.
print(generated_function("Joaquin Clasen"))  ## Output: J.C.
print(generated_function("Samuel Richert"))  ## Output: S.R.
print(generated_function("Malissa Marcus"))  ## Output: M.M.
print(generated_function("Alaina Partida"))  ## Output: A.P.
print(generated_function("Trinidad Mulloy"))  ## Output: T.M.
print(generated_function("Carlene Garrard"))  ## Output: C.G.
print(generated_function("Melodi Chism"))  ## Output: M.C.
print(generated_function("Bess Chilcott"))  ## Output: B.C.
print(generated_function("Chong Aylward"))  ## Output: C.A.
print(generated_function("Jani Ramthun"))  ## Output: J.R.
print(generated_function("Jacquiline Heintz"))  ## Output: J.H.
print(generated_function("Hayley Marquess"))  ## Output: H.M.
print(generated_function("Andria Spagnoli"))  ## Output: A.S.
print(generated_function("Irwin Covelli"))  ## Output: I.C.
print(generated_function("Gertude Montiel"))  ## Output: G.M.
print(generated_function("Stefany Reily"))  ## Output: S.R.
print(generated_function("Rae Mcgaughey"))  ## Output: R.M.
print(generated_function("Cruz Latimore"))  ## Output: C.L.
print(generated_function("Maryann Casler"))  ## Output: M.C.
print(generated_function("Annalisa Gregori"))  ## Output: A.G.
print(generated_function("Jenee Pannell"))  ## Output: J.P.


print(generated_function("Ava Bennett"))  ### Output: A.B.
print(generated_function("Isabella Brooks"))  ### Output: I.B.
print(generated_function("Jackson Turner"))  ### Output: J.T.
print(generated_function("Carter Edwards"))  ### Output: C.E.
print(generated_function("Hannah Martin"))  ### Output: H.M.
print(generated_function("Lily Anderson"))  ### Output: L.A.
print(generated_function("Scarlett Walker"))  ### Output: S.W.
print(generated_function("Amelia Nelson"))  ### Output: A.N.
print(generated_function("Madison Foster"))  ### Output: M.F.
print(generated_function("Olivia Parker"))  ### Output: O.P.
print(generated_function("Mason Thompson"))  ### Output: M.T.
print(generated_function("Caleb Mitchell"))  ### Output: C.M.
print(generated_function("Sophia Coleman"))  ### Output: S.C.
print(generated_function("Emma Reynolds"))  ### Output: E.R.
print(generated_function("Chloe Adams"))  ### Output: C.A.
print(generated_function("Samuel Wright"))  ### Output: S.W.
print(generated_function("Aiden Clark"))  ### Output: A.C.
print(generated_function("Gabriel Hayes"))  ### Output: G.H.
print(generated_function("Wyatt Davis"))  ### Output: W.D.
print(generated_function("Grace Harrison"))  ### Output: G.H.
print(generated_function("Harper Taylor"))  ### Output: H.T.
print(generated_function("Owen Morgan"))  ### Output: O.M.
print(generated_function("Nolan Cooper"))  ### Output: N.C.
print(generated_function("Elijah Foster"))  ### Output: E.F.
print(generated_function("Zoey Turner"))  ### Output: Z.T.
print(generated_function("Abigail Cooper"))  ### Output: A.C.
print(generated_function("Liam Carter"))  ### Output: L.C.
print(generated_function("Logan Smith"))  ### Output: L.S.
print(generated_function("Benjamin Hayes"))  ### Output: B.H.
print(generated_function("Caleb Johnson"))  ### Output: C.J.

# TEST SCRIPTS APPENDED!

