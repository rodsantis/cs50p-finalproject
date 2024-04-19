import game_struct
import get_movie
import sys

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

   # The director and actor variable I tought of doing the following
   # for name in actor.split(", "):
   # print(name)
   # in order to display to the user

   play = 3

   print(title)

   while play > 0:
      if play == 3:
         if len(director) == 1:
            print(game_struct.first_tip())
            print()
            print(f"The director of the Movie: {director}")
         else:
            print(game_struct.first_tip())
            print()
            print(f"The directors of the Movie:")
            for name in director.split(", "):
               print(name)
            print()
            guess = input("Guess the movie: ")
            if guess.lower() == title.lower():
               print()
               print(f"That is right! The movie is {title}!")
               sys.exit(f"YOU WON!")
            else:
               print()
               print(game_struct.first_wrong())
               print()
               play -= 1
               continue
      elif play == 2:
         if len(actor) == 1:
            print(game_struct.second_tip())
            print()
            print(f"The actor of the Movie: {actor}")
         else:
            print(game_struct.second_tip())
            print()
            print(f"The actors of the Movie:")
            for name in actor.split(", "):
               print(name)
            print()
            guess = input("Which movie you think it is: ")
            if guess.lower() == title.lower():
               print()
               print(f"That is right! The movie is {title}!")
               sys.exit(f"YOU WON!")
            else:
               print()
               print(game_struct.second_wrong())
               print()
               play -= 1
               continue
      elif play == 1:
         print(game_struct.third_tip())
         print()
         print(f"The year that it was released is {released_year}")
         guess = input("Which movie it is: ")
         if guess.lower() == title.lower():
               print()
               print(f"That is right! The movie is {title}!")
               sys.exit(f"YOU WON!")
         else:
            print()
            print(game_struct.third_wrong())
            print(f"Title: {title}, released on: {released_year}, with {votes} voters it got a rating of: {rating}!")
            play -= 1
            continue
   print()
   print(game_struct.thank_you())
   



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