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

    # Getting the stars of the movie
    stars_information = get_stars(conn, movie_title)
    if stars_information is None:
        print(f"There is no star in this Movie reported")
    else:    
        for j in range(len(stars_information)):
            print(f"Star ID: {stars_information[j]['id']}, Star Name: {stars_information[j]['name']}")

    # Getting the rating for the movie
    rating_information = get_rating(conn, movie_title)
    if rating_information is None:
        print(f"There is no rating recorded for this Movie yet")
    else:    
        for k in range(len(rating_information)):
            print(f"Rating: {rating_information[k]['rating']}, Votes: {rating_information[k]['votes']}")


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
        :return: a List of Dictionaries with the k/v as 'id' and 'name'
    """
    # Getting Director information
    director_cur = conn.cursor()
    director_cur.execute("SELECT people.id, people.name FROM people, directors, movies WHERE movies.id = directors.movie_id AND directors.person_id = people.id AND title = ?", (movie,))
    # Getting the values of the director
    director_info = director_cur.fetchall()
    # Use the print below to verify how many directors was found
    # print(len(director_info))
    if len(director_info) == 0:
        return None
    else:
        director_list = []
        for i in range(len(director_info)):
            director_dict = {'id': director_info[i][0], 'name': director_info[i][1]}
            director_list.append(director_dict)
        # Use the print below to verify the List of Dictionaries created    
        # print(director_info)
        return director_list
            

def get_stars(conn, movie):
    """
        Query people table to get the Actors of the movie
        using the movie_id and joining the tables through stars table
        :return: a List of Dictionaries with the k/v as 'id' and 'name'
    """
    # Getting stars information
    star_cur = conn.cursor()
    star_cur.execute("SELECT people.id, people.name FROM people, stars, movies WHERE movies.id = stars.movie_id AND stars.person_id = people.id AND title = ?", (movie,))
    # Storing stars information
    star_info = star_cur.fetchall()

    if len(star_info) == 0:
        return None
    else:
        star_list = []
        for i in range(len(star_info)):
            star_dict = {'id': star_info[i][0], 'name': star_info[i][1]}
            star_list.append(star_dict)

    return star_list


def get_rating(conn, movie):
    """
        Query ratings table to get the ratings of the movie
        using the movie_id and joining the tables through rstings table
        :return: a List of Dictionaries with the k/v as 'rating' and 'votes'
    """
    rating_cur = conn.cursor()
    rating_cur.execute("SELECT ratings.rating, ratings.votes FROM ratings, movies WHERE movies.id = ratings.movie_id AND title = ?", (movie,))
    rating_info = rating_cur.fetchall()
    
    if len(rating_info) == 0:
        return None
    else:
        rating_list = []
        for i in range(len(rating_info)):
            rating_dict = {'rating': rating_info[i][0], 'votes': rating_info[i][1]}
            rating_list.append(rating_dict)

    return rating_list

if __name__ == "__main__":
    main()