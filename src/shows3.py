'''
Created on Nov. 30, 2023
Returns a show with data and a cast list
@author: Sebastian
'''
import json

def load_json(filename) :
    """
    Load JSON from a file
    """
    file = open(filename,"r")
    return json.load(file)

def find_show(query, shows):
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    eg. query = friends would return Friends
    """
    for key in shows:
        if query.lower() in key.lower():
            return key
    return None

def get_show_data_by_name(show_name, shows) :
    """
    Return the data for a show based on its name
    """
    data = shows[show_name]
    return(data)

def format_show_details(show) :
    """
    Format the show details
    eg. simpsons returns 
    The Simpsons (1989 - ?, comedy, family)

    """
    start = show['premiered'][:4] #cuts off none year data
    end = show['ended']
    if end == None: #replaces unknown info with question mark
        end = "?"
    else : #cuts off the non year data
        end = end[:4]
    name = show["name"]
    
    genres = ", ".join(show["genres"]).lower() #turns a list into a string
    return f"{name} ({start} - {end}, {genres})"

def get_cast_by_id(show_id) :
    """
    Get the cast for a show
    """
    
    file = load_json(f"cast/{show_id}_cast.json")
    return file

def format_cast(cast):
    """
    Format the cast
    eg. the cast of friends is 
    Jennifer Aniston as Rachel Green
    Courteney Cox as Monica Geller
    Lisa Kudrow as Phoebe Buffay
    Matt LeBlanc as Joey Tribbiani
    Matthew Perry as Chandler Bing
    David Schwimmer as Ross Geller
    """
    for entry in cast:
        print(f"{entry['person']['name']} as {entry['character']['name']}")
    
def main():
    """
    Main function 
    """
    shows = load_json("tvshows.json")
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)
    if show_name:
        data = get_show_data_by_name(show_name, shows)
        cast = get_cast_by_id(data["id"])
        print(f"Found: {format_show_details(data)}")
        print("Cast:")
        format_cast(cast)
    else:
        print("Can't find this TV show in the Top 100!")

if __name__ == '__main__':
    main()