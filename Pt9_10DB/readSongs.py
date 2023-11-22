from connect import *

# create subroutine

def read_songs():
  # select all records
  dbCursor.execute("SELECT * FROM songs")

  # fetch the selected records
  records = dbCursor.fetchall()

  for record in records:
    print(record)



if __name__ == "__main__":
  read_songs()