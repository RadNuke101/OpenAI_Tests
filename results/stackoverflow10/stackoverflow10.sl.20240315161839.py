def extract_years(input_data):
    output = []
    for item in input_data:
        date_str = item[0].split(' ')[-1]
        output.append(date_str)
    return output

input_data = [['April 1 1799'], ['April 11 1867'], ['February 12 1806'], ['February 21 1798'], ['February 28 1844 as Delaware Township'], ['February 5 1798'], ['February 7 1892 Verona Township'], ['February 9 1797'], ['January 19 1748'], ['July 10 1721 as Upper Penns Neck Township'], ['March 15 1860'], ['March 17 1870 <as Raritan Township>'], ['March 17 1874'], ['March 23 1864'], ['March 5 1867'], ['April 28th 1828']]

print(extract_years(input_data))
