import game_struct
import get_movie

def main():
   # Printing how to play the game
   print(game_struct.game_instructions())

   # Setting a variable to be used to get game data returns that will satisfy
   # the game needs in order to be playable
   game_data = None
   while True:
      game_data = get_movie.main()
      if len(game_data) < 4:
         continue
      else:
         break

   # Setting the variables with its values which will always have one value to store
   title = game_data[0][0]['title']
   released_year = game_data[0][1]['released']
   rating = game_data[3][0]['rating']
   votes = game_data[3][1]['votes']
   # Getting the sorted values from dedicated functions
   director = get_director(game_data)
   actor = get_actor(game_data)


def get_director(game_data):
   # Setting the size of the lenght for Directors so to
   # avoid keep asking during the if statement for further slow downs
   director_lenght = len(game_data[1])

   # Getting in one variable only the name or names of the directors
   if director_lenght == 1:
      director = game_data[1][0]['name']
   else:
      director = ""
      for i in range(director_lenght):
         director = director + game_data[1][i]['name'] + "," + " "
      director = director[:-2]

   return director


def get_actor(game_data):
   # Setting the size of the lenght for Actor so to
   # avoid keep asking during the if statement for further slow downs
   actors_lenght = len(game_data[2])

   # Getting in one variable only the name or names of the actors
   if actors_lenght == 1:
      actor = game_data[2][0]['name']
   else:
      actor = ""
      for i in range(actors_lenght):
         actor = actor + game_data[2][i]['name'] + "," + " "
      actor = actor[:-2]

   return actor


if __name__ == "__main__":
    main()