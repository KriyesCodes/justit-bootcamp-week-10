from connect import *

def insert__songs():
  # SongId is auto increment field so data input is not required
  # ask user for input for Title, Artist, Genre
  songTitle = input("Enter song Title: ")
  songArtist = input("Enter song Artist: ")
  songGenre = input("Enter song Genre: ")

  # insert data into the songs table

  dbCursor.execute("""INSERT INTO songs(Title, Artist, Genre) 
VALUES(?,?,?)""", (songTitle, songArtist, songGenre))
  
  # COMMIT THE CHANGE

  dbCon.commit()
  
  # testing
  print(f"{songTitle} inserted into songs table")

if __name__ == "__main__":
  insert__songs()