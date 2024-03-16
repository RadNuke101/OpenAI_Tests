def add_title(names):
    return ['Dr. ' + name[0].split()[0] for name in names]

# Test the function with the given input
input_data = [['Launa Withers'], ['Launa Withers'], ['Launa Withers'], ['Lakenya Edison'], ['Lakenya Edison'], ['Lakenya Edison'], ['Brendan Hage'], ['Brendan Hage'], ['Brendan Hage'], ['Bradford Lango'], ['Bradford Lango'], ['Bradford Lango'], ['Rudolf Akiyama'], ['Rudolf Akiyama'], ['Rudolf Akiyama'], ['Lara Constable'], ['Lara Constable'], ['Lara Constable'], ['Madelaine Ghoston'], ['Madelaine Ghoston'], ['Madelaine Ghoston'], ['Salley Hornak'], ['Salley Hornak'], ['Salley Hornak'], ['Micha Junkin'], ['Micha Junkin'], ['Micha Junkin'], ['Teddy Bobo'], ['Teddy Bobo'], ['Teddy Bobo'], ['Coralee Scalia'], ['Coralee Scalia'], ['Coralee Scalia'], ['Jeff Quashie'], ['Jeff Quashie'], ['Jeff Quashie'], ['Vena Babiarz'], ['Vena Babiarz'], ['Vena Babiarz'], ['Karrie Lain'], ['Karrie Lain'], ['Karrie Lain'], ['Tobias Dermody'], ['Tobias Dermody'], ['Tobias Dermody'], ['Celsa Hopkins'], ['Celsa Hopkins'], ['Celsa Hopkins'], ['Kimberley Halpern'], ['Kimberley Halpern'], ['Kimberley Halpern'], ['Phillip Rowden'], ['Phillip Rowden'], ['Phillip Rowden'], ['Elias Neil'], ['Elias Neil'], ['Elias Neil'], ['Lashanda Cortes'], ['Lashanda Cortes'], ['Lashanda Cortes'], ['Mackenzie Spell'], ['Mackenzie Spell'], ['Mackenzie Spell'], ['Kathlyn Eccleston'], ['Kathlyn Eccleston'], ['Kathlyn Eccleston'], ['Georgina Brescia'], ['Georgina Brescia'], ['Georgina Brescia'], ['Beata Miah'], ['Beata Miah'], ['Beata Miah'], ['Desiree Seamons'], ['Desiree Seamons'], ['Desiree Seamons'], ['Jeanice Soderstrom'], ['Jeanice Soderstrom'], ['Jeanice Soderstrom'], ['Mariel Jurgens'], ['Mariel Jurgens'], ['Mariel Jurgens'], ['Alida Bogle'], ['Alida Bogle'], ['Alida Bogle'], ['Jacqualine Olague'], ['Jacqualine Olague'], ['Jacqualine Olague'], ['Joaquin Clasen'], ['Joaquin Clasen'], ['Joaquin Clasen'], ['Samuel Richert'], ['Samuel Richert'], ['Samuel Richert'], ['Malissa Marcus'], ['Malissa Marcus'], ['Malissa Marcus'], ['Alaina Partida'], ['Alaina Partida'], ['Alaina Partida'], ['Trinidad Mulloy'], ['Trinidad Mulloy'], ['Trinidad Mulloy'], ['Carlene Garrard'], ['Carlene Garrard'], ['Carlene Garrard'], ['Melodi Chism'], ['Melodi Chism'], ['Melodi Chism'], ['Bess Chilcott'], ['Bess Chilcott'], ['Bess Chilcott'], ['Chong Aylward'], ['Chong Aylward'], ['Chong Aylward'], ['Jani Ramthun'], ['Jani Ramthun'], ['Jani Ramthun'], ['Jacquiline Heintz'], ['Jacquiline Heintz'], ['Jacquiline Heintz'], ['Hayley Marquess'], ['Hayley Marquess'], ['Hayley Marquess'], ['Andria Spagnoli'], ['Andria Spagnoli'], ['Andria Spagnoli'], ['Irwin Covelli'], ['Irwin Covelli'], ['Irwin Covelli'], ['Gertude Montiel'], ['Gertude Montiel'], ['Gertude Montiel'], ['Stefany Reily'], ['Stefany Reily'], ['Stefany Reily'], ['Rae Mcgaughey'], ['Rae Mcgaughey'], ['Rae Mcgaughey'], ['Cruz Latimore'], ['Cruz Latimore'], ['Cruz Latimore'], ['Maryann Casler'], ['Maryann Casler'], ['Maryann Casler'], ['Annalisa Gregori'], ['Annalisa Gregori'], ['Annalisa Gregori'], ['Jenee Pannell'], ['Jenee Pannell'], ['Jenee Pannell']]
expected_output = ['Dr. Launa', 'Dr. Launa', 'Dr. Launa', 'Dr. Lakenya', 'Dr. Lakenya', 'Dr. Lakenya', 'Dr. Brendan', 'Dr. Brendan', 'Dr. Brendan', 'Dr. Bradford', 'Dr. Bradford', 'Dr. Bradford', 'Dr. Rudolf', 'Dr. Rudolf', 'Dr. Rudolf', 'Dr. Lara', 'Dr. Lara', 'Dr. Lara', 'Dr. Madelaine', 'Dr. Madelaine', 'Dr. Madelaine', 'Dr. Salley', 'Dr. Salley', 'Dr. Salley', 'Dr. Micha', 'Dr. Micha', 'Dr. Micha', 'Dr. Teddy', 'Dr. Teddy', 'Dr. Teddy', 'Dr. Coralee', 'Dr. Coralee', 'Dr. Coralee', 'Dr. Jeff', 'Dr. Jeff', 'Dr. Jeff', 'Dr. Vena', 'Dr. Vena', 'Dr. Vena', 'Dr. Karrie', 'Dr. Karrie', 'Dr. Karrie', 'Dr. Tobias', 'Dr. Tobias', 'Dr. Tobias', 'Dr. Celsa', 'Dr. Celsa', 'Dr. Celsa', 'Dr. Kimberley', 'Dr. Kimberley', 'Dr. Kimberley', 'Dr. Phillip', 'Dr. Phillip', 'Dr. Phillip', 'Dr. Elias', 'Dr. Elias', 'Dr. Elias', 'Dr. Lashanda', 'Dr. Lashanda', 'Dr. Lashanda', 'Dr. Mackenzie', 'Dr. Mackenzie', 'Dr. Mackenzie', 'Dr. Kathlyn', 'Dr. Kathlyn', 'Dr. Kathlyn', 'Dr. Georgina', 'Dr. Georgina', 'Dr. Georgina', 'Dr. Beata', 'Dr. Beata', 'Dr. Beata', 'Dr. Desiree', 'Dr. Desiree', 'Dr. Desiree', 'Dr. Jeanice', 'Dr. Jeanice', 'Dr. Jeanice', 'Dr. Mariel', 'Dr. Mariel', 'Dr. Mariel', 'Dr. Alida', 'Dr. Alida', 'Dr. Alida', 'Dr. Jacqualine', 'Dr. Jacqualine', 'Dr. Jacqualine', 'Dr. Joaquin', 'Dr. Joaquin', 'Dr. Joaquin', 'Dr. Samuel', 'Dr. Samuel', 'Dr. Samuel', 'Dr. Malissa', 'Dr. Malissa', 'Dr. Malissa', 'Dr. Alaina', 'Dr. Alaina', 'Dr. Alaina', 'Dr. Trinidad', 'Dr. Trinidad', 'Dr. Trinidad', 'Dr. Carlene', 'Dr. Carlene', 'Dr. Carlene', 'Dr. Melodi', 'Dr. Melodi', 'Dr. Melodi', 'Dr. Bess', 'Dr. Bess', 'Dr. Bess', 'Dr. Chong', 'Dr. Chong', 'Dr. Chong', 'Dr. Jani', 'Dr. Jani', 'Dr. Jani', 'Dr. Jacquiline', 'Dr. Jacquiline', 'Dr. Jacquiline', 'Dr. Hayley', 'Dr. Hayley', 'Dr. Hayley', 'Dr. Andria', 'Dr. Andria', 'Dr. Andria', 'Dr. Irwin', 'Dr. Irwin', 'Dr. Irwin', 'Dr. Gertude', 'Dr. Gertude', 'Dr. Gertude', 'Dr. Stefany', 'Dr. Stefany', 'Dr. Stefany', 'Dr. Rae', 'Dr. Rae', 'Dr. Rae', 'Dr. Cruz', 'Dr. Cruz', 'Dr. Cruz', 'Dr. Maryann', 'Dr. Maryann', 'Dr. Maryann', 'Dr. Annalisa', 'Dr. Annalisa', 'Dr. Annalisa', 'Dr. Jenee', 'Dr. Jenee', 'Dr. Jenee']

assert add_title(input_data) == expected_output
