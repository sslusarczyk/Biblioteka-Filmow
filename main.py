import random
from datetime import datetime

class Video:
  def __init__(self, title, year, genre, plays):
    self.title = title
    self.year = year
    self.genre = genre
    self.plays = plays

class Movie(Video):
  def __init__(self, title, year, genre, plays):
     self.title  = title
     self.year = year
     self.genre = genre
     self.plays = plays
  def __str__(self):
      return f'{self.title} {self.year} {self.genre} {self.plays}'

  def __repr__(self):
       return f'Movie(title="{self.title}", year="{self.year}", genre="{self.genre}",plays="{self.plays}")'

  def play(self, add):
       self.plays += add

  def display(self):
   return f'{self.title}({self.year})'

class Series(Video):
  def __init__(self, episode_nr, season_nr, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.episode_nr = episode_nr
         self.season_nr = season_nr

  def __str__(self):
         return f'{self.title} {self.year} {self.genre} {self.plays} {self.episode_nr} {self.season_nr}'
  def __repr__(self):
   return f'Series(title="{self.title}", year="{self.year}", genre="{self.genre}",plays="{self.plays}, episode_nr="{self.episode_nr:02}", season_nr="{self.season_nr:02}")'
  def play(self, add):
       self.plays += add
  def display(self):
   return f'{self.title}S{self.season_nr:02}E{self.episode_nr:02}'

my_list = [
  Movie(title="Inception", year=2010, genre="Sci-Fi", plays=100),
  Series(title="Game of Thrones", year=2011, genre="Fantasy", plays=200, episode_nr=1, season_nr=1),
  Movie(title="The Dark Knight", year=2008, genre="Action", plays=150),
  Series(title="Stranger Things", year=2016, genre="Sci-Fi", plays=120, episode_nr=1, season_nr=1),
  Movie(title="Inception 2", year=2010, genre="Sci-Fi", plays=10),
  Series(title="Game of Thrones 2", year=2011, genre="Fantasy", plays=20, episode_nr=1, season_nr=1),
  Movie(title="The Dark Knight 2", year=2008, genre="Action", plays=15),
  Series(title="Stranger Things 2", year=2016, genre="Sci-Fi", plays=12, episode_nr=1, season_nr=1),
]
def get_movies(objects_list):
  return [obj for obj in objects_list if isinstance(obj, Movie)]
def get_series(objects_list):
  return [obj for obj in objects_list if isinstance(obj, Series)]
def search(objects_list, search_function):
  return [obj for obj in objects_list if search_function.lower() in obj.title.lower()]

def generate_views(objects_list):
  selected_obj = random.choice(my_list)
  selected_nr = random.randint(1, 100)
  selected_obj.play(selected_nr)
def generate_10(obj):
  for _ in range (10):
    generate_views(obj)
  print(f"Biblioteka filmow po generacji: {my_list}")
def top_titles(object_list,class_type, n=3):
  filtered_objects = [obj for obj in object_list if isinstance(obj, class_type)]
  if not filtered_objects:
      return []
  sorted_objects = sorted(filtered_objects, key=lambda x: x.plays if isinstance(x, Video) else x.plays, reverse=True)
  return sorted_objects[:n]


print(f"Biblioteka filmow: {my_list}")

user_input = ' '
while True:

  while user_input != "N":
      type_of_movie = (input('Podaj rodzaj filmu:Serial lub Film lub Exit (S/F/E)'))
      if type_of_movie == 'F':
        print('Wybrales film')
        title = input('Podaj tytul filmu:')
        year = int(input('Podaj rok wydania:'))
        genre = input('Podaj gatunek filmu:')
        plays = int(input('Podaj liczbe odtworzen:'))
        my_list.append(Movie(title, year, genre, plays))
      elif type_of_movie == 'S':
        print('Wybrales serial')
        title = input('Podaj tytul serialu:')
        year = int(input('Podaj rok wydania:'))
        genre = input('Podaj gatunek serialu:')
        plays = int(input('Podaj liczbe odtworzen:'))
        episode_nr = int(input('Podaj numer odcinka:'))
        season_nr = int(input('Podaj numer sezonu:'))
        my_list.append(Series(episode_nr, season_nr,title, year, genre, plays, ))
      elif type_of_movie == 'E':
        break
      print(f"Biblioteka filmow: {my_list}")
      user_input = input("Czy chcesz dodac kolejny Film lub Serial (Y/N): ")

  while user_input != "7":
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d.%m.%Y")
    user_input = input("Co chesz teraz zrobic?: \n 1. Filtruj  Filmy\n 2. Filtruj Seriale\n 3. Wyszukaj\n 4. Generuj losowa ilosc odtworzen\n 5. Wyswietl najpopularniejsze Filmy\n 6. Wyswietl najpopularniejsze Seriale\n 7. Exit\n (1/2/3/4/5/6/7)")
    if user_input == '1':
      found_movies = get_movies(my_list)
        # Print the found movies
      print(f"Znalaziono {Movie.__name__} obiekty:")
      for movie in found_movies:
          print(movie)
    elif user_input == '2':
      found_series = get_series(my_list)
        # Print the found movies
      print(f"Znalaziono {Series.__name__} obiekty:")
      for series in found_series:
          print(series)
    elif user_input == '3':
      user_input = input("Podaj tytul filmu: ")
      found_movies = search(my_list, user_input)
      if found_movies:
          print("Znaleziono film:")
          for movie in found_movies:
              print(movie)
      else:
          print("Nie znaleziono takiego filmu")
          break
    elif user_input == '4':
      generate_10(my_list)
    elif user_input == '5':
      top_objects = top_titles(my_list, Movie, 3)
      print(f"Najpopularniejsze filmy z dnia:{formatted_date}")
      for obj in top_objects:
        if isinstance(obj, Video):
          print(f"Tytul Filmu: {obj.title}, Obejrzen: {obj.plays}")
    elif user_input == '6':
      top_objects = top_titles(my_list, Series, 3)
      print(f"Najpopularniejsze filmy z dnia:{formatted_date}")
      for obj in top_objects:
        if isinstance(obj, Series):
          print(f"Tytul Filmu: {obj.title}, Obejrzen: {obj.plays}")
    elif user_input == '7':
      break



