import sqlite3
import os

def main():
    #Getting the current path and assigning the database file to a variable
    path = os.path.realpath(__file__)
    path = path.replace('get_movie.py', 'movies.db')
    database = path

    conn = connection(database)
    
    # Getting the movie information via random()
    movie_id, movie_title, movie_year = select_movie(conn)
    print(f"Movie ID:{movie_id}, Movie Title:{movie_title}, Released year:{movie_year}")

    # Getting the director information
    director_information = get_director(conn, movie_title)
    # Use the print below to check the returned List of dictionaries
    # print(director_information)
    if director_information is None:
        print(f"No directors for this Movie reported")
    else: 
        for i in range(len(director_information)):
            print(f"Director ID: {director_information[i]['id']}, Director Name: {director_information[i]['name']}")


def connection(database):
    """
        Create a database connection to the SQLite database
    """
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as err:
        print(err)

    return conn


def select_movie(conn):
    """
        Querry movies Table for the Movie name, id and year randongly
    """
    # Movie and year Cursor
    movie_cur = conn.cursor()
    movie_cur.execute("SELECT id, title, year FROM movies ORDER BY random() LIMIT 1")
    # Getting the values of the Movie name and the Released year
    film = movie_cur.fetchall()
    movie_id, movie_name, release_year = film[0]

    return movie_id, movie_name, release_year


def get_director(conn, movie):
    """
        Query people table to get the Director of the movie
        using the movie_id and joining the tables through directors table
        IF there is no Director > function will return None
    """
    # Getting Director information
    director_cur = conn.cursor()
    director_cur.execute("SELECT people.id, people.name FROM people, directors, movies WHERE movies.id = directors.movie_id AND directors.person_id = people.id AND title = ?", (movie,))
    # Getting the valurs of the director
    director_info = director_cur.fetchall()
    # Use the print below to verify how many directors was found
    # print(len(director_info))
    if len(director_info) == 0:
        return None
    elif len(director_info) == 1:
        director_id, director_name = director_info[0]
        return [{'id': director_id, 'name': director_name}]
    else:
        director_list = []
        for i in range(len(director_info)):
            director_dict = {'id': director_info[i][0], 'name': director_info[i][1]}
            director_list.append(director_dict)
        # Use the print below to verify the List of Dictionaries created    
        # print(director_info)
        return director_list
            



if __name__ == "__main__":
    main()