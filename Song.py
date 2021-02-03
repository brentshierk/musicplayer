class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # Getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # Setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = title


  # Getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  # Setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title


  # Return a string of the song title.
  def __str__(self):
    return self.__title


  # Return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f'{self.__title} -> {self.__next_song.__title}'