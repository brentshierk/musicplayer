from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #creates a new node  
    new_song = Song(title)
    #setting the new song to be the head of the list
    new_song.next = self.__first_song
    self.__first_song = new_song
    print('new song added')
    




  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    index = 0
    current_song = self.__first_song
    while current_song != None:
      if current_song.get_title() == title:
        return index
      else:
        current_song == current_song.get_next_song()
        index += 1
    return None
      

    # if self.__first_song == None:
    #   return None
    # elif current_song == self.title:
    #   return(f"found at index {self.}")


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
      current_song = self.__first_song
      if current_song and current_song.__title == title:
        current_song = current_song.set_next_song

    
    



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    counter = 0
    current_node = self.__first_song

    while current_node != None:
      counter += 1
      current_node = current_node.next
    return counter



  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

    def print_songs(self):
      counter= 1
      current_song = self.__first_song
      while current_song != None:
        print(f"{counter}. {current_song} {counter}")
        current_song = current_song.get_next_song()
        counter += 1
      
  