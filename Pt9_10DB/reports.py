from connect import *
 
# create subroutine
def reports():
    dbCursor.execute("SELECT Artist FROM songs WHERE SongID = 2")
 
    reportsData = dbCursor.fetchall()
    # print(type(reportsData))
    # print(type(reportsData[0]))
    # print(reportsData)
    for records in reportsData:
        print(records)
if __name__ == "__main__":
    reports()