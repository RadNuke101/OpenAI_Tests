# Start time: 2024-04-10 17:42:05.112926

'''
Prompt:
Given that input as ['Launa', 'Withers'] output is Launa Withers, input as ['Lakenya', 'Edison'] output is Lakenya Edison, input as ['Brendan', 'Hage'] output is Brendan Hage, input as ['Bradford', 'Lango'] output is Bradford Lango, input as ['Rudolf', 'Akiyama'] output is Rudolf Akiyama, input as ['Lara', 'Constable'] output is Lara Constable, input as ['Madelaine', 'Ghoston'] output is Madelaine Ghoston, input as ['Salley', 'Hornak'] output is Salley Hornak, input as ['Micha', 'Junkin'] output is Micha Junkin, input as ['Teddy', 'Bobo'] output is Teddy Bobo, input as ['Coralee', 'Scalia'] output is Coralee Scalia, input as ['Jeff', 'Quashie'] output is Jeff Quashie, input as ['Vena', 'Babiarz'] output is Vena Babiarz, input as ['Karrie', 'Lain'] output is Karrie Lain, input as ['Tobias', 'Dermody'] output is Tobias Dermody, input as ['Celsa', 'Hopkins'] output is Celsa Hopkins, input as ['Kimberley', 'Halpern'] output is Kimberley Halpern, input as ['Phillip', 'Rowden'] output is Phillip Rowden, input as ['Elias', 'Neil'] output is Elias Neil, input as ['Lashanda', 'Cortes'] output is Lashanda Cortes, input as ['Mackenzie', 'Spell'] output is Mackenzie Spell, input as ['Kathlyn', 'Eccleston'] output is Kathlyn Eccleston, input as ['Georgina', 'Brescia'] output is Georgina Brescia, input as ['Beata', 'Miah'] output is Beata Miah, input as ['Desiree', 'Seamons'] output is Desiree Seamons, input as ['Jeanice', 'Soderstrom'] output is Jeanice Soderstrom, input as ['Mariel', 'Jurgens'] output is Mariel Jurgens, input as ['Alida', 'Bogle'] output is Alida Bogle, input as ['Jacqualine', 'Olague'] output is Jacqualine Olague, input as ['Joaquin', 'Clasen'] output is Joaquin Clasen, input as ['Samuel', 'Richert'] output is Samuel Richert, input as ['Malissa', 'Marcus'] output is Malissa Marcus, input as ['Alaina', 'Partida'] output is Alaina Partida, input as ['Trinidad', 'Mulloy'] output is Trinidad Mulloy, input as ['Carlene', 'Garrard'] output is Carlene Garrard, input as ['Melodi', 'Chism'] output is Melodi Chism, input as ['Bess', 'Chilcott'] output is Bess Chilcott, input as ['Chong', 'Aylward'] output is Chong Aylward, input as ['Jani', 'Ramthun'] output is Jani Ramthun, input as ['Jacquiline', 'Heintz'] output is Jacquiline Heintz, input as ['Hayley', 'Marquess'] output is Hayley Marquess, input as ['Andria', 'Spagnoli'] output is Andria Spagnoli, input as ['Irwin', 'Covelli'] output is Irwin Covelli, input as ['Gertude', 'Montiel'] output is Gertude Montiel, input as ['Stefany', 'Reily'] output is Stefany Reily, input as ['Rae', 'Mcgaughey'] output is Rae Mcgaughey, input as ['Cruz', 'Latimore'] output is Cruz Latimore, input as ['Maryann', 'Casler'] output is Maryann Casler, input as ['Annalisa', 'Gregori'] output is Annalisa Gregori, input as ['Jenee', 'Pannell'] output is Jenee Pannell, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        first_name = input_list[0][2:-1]
        last_name = input_list[1][1:-2]
        return first_name + ' ' + last_name
    except:
        return "Invalid input format"

# Test cases
print(generated_function("['Launa', 'Withers']"))
print(generated_function("['Lakenya', 'Edison']"))
print(generated_function("['Brendan', 'Hage']"))
print(generated_function("['Bradford', 'Lango']"))
print(generated_function("['Rudolf', 'Akiyama']"))
print(generated_function("['Lara', 'Constable']"))
print(generated_function("['Madelaine', 'Ghoston']"))
print(generated_function("['Salley', 'Hornak']"))
print(generated_function("['Micha', 'Junkin']"))
print(generated_function("['Teddy', 'Bobo']"))
print(generated_function("['Coralee', 'Scalia']"))
print(generated_function("['Jeff', 'Quashie']"))
print(generated_function("['Vena', 'Babiarz']"))
print(generated_function("['Karrie', 'Lain']"))
print(generated_function("['Tobias', 'Dermody']"))
print(generated_function("['Celsa', 'Hopkins']"))
print(generated_function("['Kimberley', 'Halpern']"))
print(generated_function("['Phillip', 'Rowden']"))
print(generated_function("['Elias', 'Neil']"))
print(generated_function("['Lashanda', 'Cortes']"))
print(generated_function("['Mackenzie', 'Spell']"))
print(generated_function("['Kathlyn', 'Eccleston']"))
print(generated_function("['Georgina', 'Brescia']"))
print(generated_function("['Beata', 'Miah']"))
print(generated_function("['Desiree', 'Seamons']"))
print(generated_function("['Jeanice', 'Soderstrom']"))
print(generated_function("['Mariel', 'Jurgens']"))
print(generated_function("['Alida', 'Bogle']"))
print(generated_function("['Jacqualine', 'Olague']"))
print(generated_function("['Joaquin', 'Clasen']"))
print(generated_function("['Samuel', 'Richert']"))
print(generated_function("['Malissa', 'Marcus']"))
print(generated_function("['Alaina', 'Partida']"))
print(generated_function("['Trinidad', 'Mulloy']"))
print(generated_function("['Carlene', 'Garrard']"))
print(generated_function("['Melodi', 'Chism']"))
print(generated_function("['Bess', 'Chilcott']"))
print(generated_function("['Chong', 'Aylward']"))
print(generated_function("['Jani', 'Ramthun']"))
print(generated_function("['Jacquiline', 'Heintz']"))
print(generated_function("['Hayley', 'Marquess']"))
print(generated_function("['Andria', 'Spagnoli']"))
print(generated_function("['Irwin', 'Covelli']"))
print(generated_function("['Gertude', 'Montiel']"))
print(generated_function("['Stefany', 'Reily']"))
print(generated_function("['Rae', 'Mcgaughey']"))
print(generated_function("['Cruz', 'Latimore']"))
print(generated_function("['Maryann', 'Casler']"))
print(generated_function("['Annalisa', 'Gregori']"))
print(generated_function("['Jenee', 'Pannell']"))
print(generated_function("Launa", "Withers"))  ## Output: Launa Withers
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya Edison
print(generated_function("Brendan", "Hage"))  ## Output: Brendan Hage
print(generated_function("Bradford", "Lango"))  ## Output: Bradford Lango
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf Akiyama
print(generated_function("Lara", "Constable"))  ## Output: Lara Constable
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine Ghoston
print(generated_function("Salley", "Hornak"))  ## Output: Salley Hornak
print(generated_function("Micha", "Junkin"))  ## Output: Micha Junkin
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy Bobo
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee Scalia
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Quashie
print(generated_function("Vena", "Babiarz"))  ## Output: Vena Babiarz
print(generated_function("Karrie", "Lain"))  ## Output: Karrie Lain
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias Dermody
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa Hopkins
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley Halpern
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip Rowden
print(generated_function("Elias", "Neil"))  ## Output: Elias Neil
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda Cortes
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie Spell
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn Eccleston
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina Brescia
print(generated_function("Beata", "Miah"))  ## Output: Beata Miah
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree Seamons
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice Soderstrom
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel Jurgens
print(generated_function("Alida", "Bogle"))  ## Output: Alida Bogle
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine Olague
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin Clasen
print(generated_function("Samuel", "Richert"))  ## Output: Samuel Richert
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa Marcus
print(generated_function("Alaina", "Partida"))  ## Output: Alaina Partida
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad Mulloy
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene Garrard
print(generated_function("Melodi", "Chism"))  ## Output: Melodi Chism
print(generated_function("Bess", "Chilcott"))  ## Output: Bess Chilcott
print(generated_function("Chong", "Aylward"))  ## Output: Chong Aylward
print(generated_function("Jani", "Ramthun"))  ## Output: Jani Ramthun
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline Heintz
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley Marquess
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria Spagnoli
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin Covelli
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude Montiel
print(generated_function("Stefany", "Reily"))  ## Output: Stefany Reily
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae Mcgaughey
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz Latimore
print(generated_function("Maryann", "Casler"))  ## Output: Maryann Casler
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa Gregori
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee Pannell

# End time: 2024-04-10 17:42:13.530657
# Elapsed time in seconds: 8.417631805999918


# APPEND TEST SCRIPTS...
print(generated_function("Launa", "Withers"))  ## Output: Launa Withers
print(generated_function("Lakenya", "Edison"))  ## Output: Lakenya Edison
print(generated_function("Brendan", "Hage"))  ## Output: Brendan Hage
print(generated_function("Bradford", "Lango"))  ## Output: Bradford Lango
print(generated_function("Rudolf", "Akiyama"))  ## Output: Rudolf Akiyama
print(generated_function("Lara", "Constable"))  ## Output: Lara Constable
print(generated_function("Madelaine", "Ghoston"))  ## Output: Madelaine Ghoston
print(generated_function("Salley", "Hornak"))  ## Output: Salley Hornak
print(generated_function("Micha", "Junkin"))  ## Output: Micha Junkin
print(generated_function("Teddy", "Bobo"))  ## Output: Teddy Bobo
print(generated_function("Coralee", "Scalia"))  ## Output: Coralee Scalia
print(generated_function("Jeff", "Quashie"))  ## Output: Jeff Quashie
print(generated_function("Vena", "Babiarz"))  ## Output: Vena Babiarz
print(generated_function("Karrie", "Lain"))  ## Output: Karrie Lain
print(generated_function("Tobias", "Dermody"))  ## Output: Tobias Dermody
print(generated_function("Celsa", "Hopkins"))  ## Output: Celsa Hopkins
print(generated_function("Kimberley", "Halpern"))  ## Output: Kimberley Halpern
print(generated_function("Phillip", "Rowden"))  ## Output: Phillip Rowden
print(generated_function("Elias", "Neil"))  ## Output: Elias Neil
print(generated_function("Lashanda", "Cortes"))  ## Output: Lashanda Cortes
print(generated_function("Mackenzie", "Spell"))  ## Output: Mackenzie Spell
print(generated_function("Kathlyn", "Eccleston"))  ## Output: Kathlyn Eccleston
print(generated_function("Georgina", "Brescia"))  ## Output: Georgina Brescia
print(generated_function("Beata", "Miah"))  ## Output: Beata Miah
print(generated_function("Desiree", "Seamons"))  ## Output: Desiree Seamons
print(generated_function("Jeanice", "Soderstrom"))  ## Output: Jeanice Soderstrom
print(generated_function("Mariel", "Jurgens"))  ## Output: Mariel Jurgens
print(generated_function("Alida", "Bogle"))  ## Output: Alida Bogle
print(generated_function("Jacqualine", "Olague"))  ## Output: Jacqualine Olague
print(generated_function("Joaquin", "Clasen"))  ## Output: Joaquin Clasen
print(generated_function("Samuel", "Richert"))  ## Output: Samuel Richert
print(generated_function("Malissa", "Marcus"))  ## Output: Malissa Marcus
print(generated_function("Alaina", "Partida"))  ## Output: Alaina Partida
print(generated_function("Trinidad", "Mulloy"))  ## Output: Trinidad Mulloy
print(generated_function("Carlene", "Garrard"))  ## Output: Carlene Garrard
print(generated_function("Melodi", "Chism"))  ## Output: Melodi Chism
print(generated_function("Bess", "Chilcott"))  ## Output: Bess Chilcott
print(generated_function("Chong", "Aylward"))  ## Output: Chong Aylward
print(generated_function("Jani", "Ramthun"))  ## Output: Jani Ramthun
print(generated_function("Jacquiline", "Heintz"))  ## Output: Jacquiline Heintz
print(generated_function("Hayley", "Marquess"))  ## Output: Hayley Marquess
print(generated_function("Andria", "Spagnoli"))  ## Output: Andria Spagnoli
print(generated_function("Irwin", "Covelli"))  ## Output: Irwin Covelli
print(generated_function("Gertude", "Montiel"))  ## Output: Gertude Montiel
print(generated_function("Stefany", "Reily"))  ## Output: Stefany Reily
print(generated_function("Rae", "Mcgaughey"))  ## Output: Rae Mcgaughey
print(generated_function("Cruz", "Latimore"))  ## Output: Cruz Latimore
print(generated_function("Maryann", "Casler"))  ## Output: Maryann Casler
print(generated_function("Annalisa", "Gregori"))  ## Output: Annalisa Gregori
print(generated_function("Jenee", "Pannell"))  ## Output: Jenee Pannell


print(generated_function("Jackson", "Turner"))  ### Output: Jackson Turner
print(generated_function("Nolan", "Cooper"))  ### Output: Nolan Cooper
print(generated_function("Zoey", "Turner"))  ### Output: Zoey Turner
print(generated_function("Wyatt", "Davis"))  ### Output: Wyatt Davis
print(generated_function("Lily", "Anderson"))  ### Output: Lily Anderson
print(generated_function("Amelia", "Nelson"))  ### Output: Amelia Nelson
print(generated_function("Elijah", "Foster"))  ### Output: Elijah Foster
print(generated_function("Samuel", "Wright"))  ### Output: Samuel Wright
print(generated_function("Mason", "Thompson"))  ### Output: Mason Thompson
print(generated_function("Carter", "Edwards"))  ### Output: Carter Edwards
print(generated_function("Abigail", "Cooper"))  ### Output: Abigail Cooper
print(generated_function("Gabriel", "Hayes"))  ### Output: Gabriel Hayes
print(generated_function("Chloe", "Adams"))  ### Output: Chloe Adams
print(generated_function("Hannah", "Martin"))  ### Output: Hannah Martin
print(generated_function("Aiden", "Clark"))  ### Output: Aiden Clark
print(generated_function("Benjamin", "Hayes"))  ### Output: Benjamin Hayes
print(generated_function("Caleb", "Mitchell"))  ### Output: Caleb Mitchell
print(generated_function("Isabella", "Brooks"))  ### Output: Isabella Brooks
print(generated_function("Ava", "Bennett"))  ### Output: Ava Bennett
print(generated_function("Sophia", "Coleman"))  ### Output: Sophia Coleman
print(generated_function("Harper", "Taylor"))  ### Output: Harper Taylor
print(generated_function("Owen", "Morgan"))  ### Output: Owen Morgan
print(generated_function("Caleb", "Johnson"))  ### Output: Caleb Johnson
print(generated_function("Madison", "Foster"))  ### Output: Madison Foster
print(generated_function("Liam", "Carter"))  ### Output: Liam Carter
print(generated_function("Grace", "Harrison"))  ### Output: Grace Harrison
print(generated_function("Emma", "Reynolds"))  ### Output: Emma Reynolds
print(generated_function("Scarlett", "Walker"))  ### Output: Scarlett Walker
print(generated_function("Logan", "Smith"))  ### Output: Logan Smith
print(generated_function("Olivia", "Parker"))  ### Output: Olivia Parker

# TEST SCRIPTS APPENDED!

