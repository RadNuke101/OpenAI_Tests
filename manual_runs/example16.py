# Function to extract data after last "/"
def extract_data(url):
    # Split the url by "/"
    split_url = url.split("/")
    # Check if there is data after last "/"
    if len(split_url[-1]) > 0:
        # Return the data after last "/"
        return split_url[-1]
    else:
        # Split the url by "www."
        split_url = url.split("www.")
        # Split the url by ".com"
        split_url = split_url[1].split(".com")
        # Return the phrase between "www." and ".com"
        return split_url[0]