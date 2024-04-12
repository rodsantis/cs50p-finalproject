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
    print(f"{movie_id}, {movie_title}, {movie_year}")

    # Getting the directors using the movie_id
    director_id, director_name = get_director(conn, movie_id)
    print(f"{director_id}, {director_name}")



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


def get_director(conn, movie_id):
    """
        Query people table to get the Director of the movie
        using the movie_id and joining the tables through directors table
        IF there is no Director > function will return None
    """
    # Director cursor and query to find id and name
    director_cur = conn.cursor()
    director_cur.execute("SELECT id, name FROM people WHERE id IN (SELECT person_id FROM directors WHERE movie_id = ?)", int(movie_id))

    director = director_cur.fetchall()
    if director[0] is None:
        return None
    else:
        director_id, director_name = director[0]


if __name__ == "__main__":
    main()