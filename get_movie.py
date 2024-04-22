import sqlite3
import os
from pathlib import Path

def main():
    """
        The function main should be called in order to get the movie data
        other functions were created and were called by the main
        all the data of the movie can be found, processed and returned by the main function
    """
    #Getting the current path and assigning the database file to a variable
    path = str(Path(__file__).parent/"movies.db")
    database = path

    # Creating connection to be used by other functions
    conn = connection(database)

    # Variable that will be returned by this file program
    game_data = []
    
    # Getting the movie information via random()
    movie_id, movie_title, movie_year = select_movie(conn)
    movie_data = [{'title': movie_title}, {'released': movie_year}]
    game_data.append(movie_data)
    
    # Getting the director information
    director_information = get_director(conn, movie_title)
    director_data = []
    if director_information is not None:
        for i in range(len(director_information)):
            director_data.append({'name': director_information[i]['name']})
        game_data.append(director_data)

    # Getting the stars of the movie
    stars_information = get_stars(conn, movie_title)
    stars_data = []
    if stars_information is not None: 
        for j in range(len(stars_information)):
            stars_data.append({'name': stars_information[j]['name']})
        game_data.append(stars_data)

    # Getting the rating for the movie
    rating_information = get_rating(conn, movie_title)
    if rating_information is not None:  
        rating_data = [{'rating': rating_information[0]['rating']}, {'votes': rating_information[0]['votes']}]
        game_data.append(rating_data)

    return game_data
    


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
    movie_cur = conn.cursor()
    movie_cur.execute("SELECT id, title, year FROM movies ORDER BY random() LIMIT 1")
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
    director_cur = conn.cursor()
    director_cur.execute("SELECT people.id, people.name FROM people, directors, movies WHERE movies.id = directors.movie_id AND directors.person_id = people.id AND title = ?", (movie,))
    director_info = director_cur.fetchall()

    if len(director_info) == 0:
        return None
    else:
        director_list = []
        for i in range(len(director_info)):
            director_dict = {'id': director_info[i][0], 'name': director_info[i][1]}
            director_list.append(director_dict)

        return director_list
            

def get_stars(conn, movie):
    """
        Query people table to get the Actors of the movie
        using the movie_id and joining the tables through stars table
        :return: a List of Dictionaries with the k/v as 'id' and 'name'
    """

    star_cur = conn.cursor()
    star_cur.execute("SELECT people.id, people.name FROM people, stars, movies WHERE movies.id = stars.movie_id AND stars.person_id = people.id AND title = ?", (movie,))
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