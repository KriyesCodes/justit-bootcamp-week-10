from connect import *

def update_songs():
  # use primary key to update a record

  idField = int(input("Enter the song ID of the record you want to update: "))

  # field to update
  fieldName = input("Enter Title or Artist or Genre as field name: ").title()

  fieldValue = input(f"Enter the value for {fieldName} field: ")

  if (fieldName == 'Title'):
    query = "UPDATE songs SET Title = ? WHERE SongID = ?"
  elif (fieldName == 'Artist'):
    query = "UPDATE songs SET Artist = ? WHERE SongID = ?"
  elif (fieldName == 'Genre'):
    query = "UPDATE songs SET Genre = ? WHERE SongID = ?"
  else:
    print("Incorrect input")
    return
  
  dbCursor.execute(query, (fieldValue, idField))

  dbCon.commit()
  
  print(f"Record {idField} updated")

if __name__ == "__main__":
  update_songs()