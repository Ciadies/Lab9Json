'''
Created on Nov. 30, 2023
Basic load json and find if a key exists within
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

def main():
    """
    Main function 
    """
    shows = load_json("tvshows.json")
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)
    if show_name:
        print(f"Found: {show_name}")
    else:
        print("Can't find this TV show in the Top 100!")

if __name__ == '__main__':
    main()