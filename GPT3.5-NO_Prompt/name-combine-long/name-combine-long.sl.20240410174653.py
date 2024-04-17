# Start time: 2024-04-10 17:53:33.611740

'''
Prompt:
Given that input as ['Launa', 'Withers'] output is Launa Withers, input as ['Lakenya', 'Edison'] output is Lakenya Edison, input as ['Brendan', 'Hage'] output is Brendan Hage, input as ['Bradford', 'Lango'] output is Bradford Lango, input as ['Rudolf', 'Akiyama'] output is Rudolf Akiyama, input as ['Lara', 'Constable'] output is Lara Constable, input as ['Madelaine', 'Ghoston'] output is Madelaine Ghoston, input as ['Salley', 'Hornak'] output is Salley Hornak, input as ['Micha', 'Junkin'] output is Micha Junkin, input as ['Teddy', 'Bobo'] output is Teddy Bobo, input as ['Coralee', 'Scalia'] output is Coralee Scalia, input as ['Jeff', 'Quashie'] output is Jeff Quashie, input as ['Vena', 'Babiarz'] output is Vena Babiarz, input as ['Karrie', 'Lain'] output is Karrie Lain, input as ['Tobias', 'Dermody'] output is Tobias Dermody, input as ['Celsa', 'Hopkins'] output is Celsa Hopkins, input as ['Kimberley', 'Halpern'] output is Kimberley Halpern, input as ['Phillip', 'Rowden'] output is Phillip Rowden, input as ['Elias', 'Neil'] output is Elias Neil, input as ['Lashanda', 'Cortes'] output is Lashanda Cortes, input as ['Mackenzie', 'Spell'] output is Mackenzie Spell, input as ['Kathlyn', 'Eccleston'] output is Kathlyn Eccleston, input as ['Georgina', 'Brescia'] output is Georgina Brescia, input as ['Beata', 'Miah'] output is Beata Miah, input as ['Desiree', 'Seamons'] output is Desiree Seamons, input as ['Jeanice', 'Soderstrom'] output is Jeanice Soderstrom, input as ['Mariel', 'Jurgens'] output is Mariel Jurgens, input as ['Alida', 'Bogle'] output is Alida Bogle, input as ['Jacqualine', 'Olague'] output is Jacqualine Olague, input as ['Joaquin', 'Clasen'] output is Joaquin Clasen, input as ['Samuel', 'Richert'] output is Samuel Richert, input as ['Malissa', 'Marcus'] output is Malissa Marcus, input as ['Alaina', 'Partida'] output is Alaina Partida, input as ['Trinidad', 'Mulloy'] output is Trinidad Mulloy, input as ['Carlene', 'Garrard'] output is Carlene Garrard, input as ['Melodi', 'Chism'] output is Melodi Chism, input as ['Bess', 'Chilcott'] output is Bess Chilcott, input as ['Chong', 'Aylward'] output is Chong Aylward, input as ['Jani', 'Ramthun'] output is Jani Ramthun, input as ['Jacquiline', 'Heintz'] output is Jacquiline Heintz, input as ['Hayley', 'Marquess'] output is Hayley Marquess, input as ['Andria', 'Spagnoli'] output is Andria Spagnoli, input as ['Irwin', 'Covelli'] output is Irwin Covelli, input as ['Gertude', 'Montiel'] output is Gertude Montiel, input as ['Stefany', 'Reily'] output is Stefany Reily, input as ['Rae', 'Mcgaughey'] output is Rae Mcgaughey, input as ['Cruz', 'Latimore'] output is Cruz Latimore, input as ['Maryann', 'Casler'] output is Maryann Casler, input as ['Annalisa', 'Gregori'] output is Annalisa Gregori, input as ['Jenee', 'Pannell'] output is Jenee Pannell, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        first_name = input_list[0][2:-1]
        last_name = input_list[1][2:-2]
        return first_name + ' ' + last_name
    except:
        return "Invalid input format"

# Test cases
print(generated_function("['Launa', 'Withers']")) # Launa Withers
print(generated_function("['Lakenya', 'Edison']")) # Lakenya Edison
print(generated_function("['Brendan', 'Hage']")) # Brendan Hage
print(generated_function("['Bradford', 'Lango']")) # Bradford Lango
print(generated_function("['Rudolf', 'Akiyama']")) # Rudolf Akiyama
print(generated_function("['Lara', 'Constable']")) # Lara Constable
print(generated_function("['Madelaine', 'Ghoston']")) # Madelaine Ghoston
print(generated_function("['Salley', 'Hornak']")) # Salley Hornak
print(generated_function("['Micha', 'Junkin']")) # Micha Junkin
print(generated_function("['Teddy', 'Bobo']")) # Teddy Bobo
print(generated_function("['Coralee', 'Scalia']")) # Coralee Scalia
print(generated_function("['Jeff', 'Quashie']")) # Jeff Quashie
print(generated_function("['Vena', 'Babiarz']")) # Vena Babiarz
print(generated_function("['Karrie', 'Lain']")) # Karrie Lain
print(generated_function("['Tobias', 'Dermody']")) # Tobias Dermody
print(generated_function("['Celsa', 'Hopkins']")) # Celsa Hopkins
print(generated_function("['Kimberley', 'Halpern']")) # Kimberley Halpern
print(generated_function("['Phillip', 'Rowden']")) # Phillip Rowden
print(generated_function("['Elias', 'Neil']")) # Elias Neil
print(generated_function("['Lashanda', 'Cortes']")) # Lashanda Cortes
print(generated_function("['Mackenzie', 'Spell']")) # Mackenzie Spell
print(generated_function("['Kathlyn', 'Eccleston']")) # Kathlyn Eccleston
print(generated_function("['Georgina', 'Brescia']")) # Georgina Brescia
print(generated_function("['Beata', 'Miah']")) # Beata Miah
print(generated_function("['Desiree', 'Seamons']")) # Desiree Seamons
print(generated_function("['Jeanice', 'Soderstrom']")) # Jeanice Soderstrom
print(generated_function("['Mariel', 'Jurgens']")) # Mariel Jurgens
print(generated_function("['Alida', 'Bogle']")) # Alida Bogle
print(generated_function("['Jacqualine', 'Olague']")) # Jacqualine Olague
print(generated_function("['Joaquin', 'Clasen']")) # Joaquin Clasen
print(generated_function("['Samuel', 'Richert']")) # Samuel Richert
print(generated_function("['Malissa', 'Marcus']")) # Malissa Marcus
print(generated_function("['Alaina', 'Partida']")) # Alaina Partida
print(generated_function("['Trinidad', 'Mulloy']")) # Trinidad Mulloy
print(generated_function("['Carlene', 'Garrard']")) # Carlene Garrard
print(generated_function("['Melodi', 'Chism']")) # Melodi Chism
print(generated_function("['Bess', 'Chilcott']")) # Bess Chilcott
print(generated_function("['Chong', 'Aylward']")) # Chong Aylward
print(generated_function("['Jani', 'Ramthun']")) # Jani Ramthun
print(generated_function("['Jacquiline', 'Heintz']")) # Jacquiline Heintz
print(generated_function("['Hayley', 'Marquess']")) # Hayley Marquess
print(generated_function("['Andria', 'Spagnoli']")) # Andria Spagnoli
print(generated_function("['Irwin', 'Covelli']")) # Irwin Covelli
print(generated_function("['Gertude', 'Montiel']")) # Gertude Montiel
print(generated_function("['Stefany', 'Reily']")) # Stefany Reily
print(generated_function("['Rae', 'Mcgaughey']")) # Rae Mcgaughey
print(generated_function("['Cruz', 'Latimore']")) # Cruz Latimore
print(generated_function("['Maryann', 'Casler']")) # Maryann Casler
print(generated_function("['Annalisa', 'Gregori']")) # Annalisa Gregori
print(generated_function("['Jenee', 'Pannell']")) # Jenee Pannell
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

# End time: 2024-04-10 17:53:50.969986
# Elapsed time in seconds: 17.35778484499997