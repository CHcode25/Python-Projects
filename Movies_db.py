#importing sqllite and logging modules
import sqlite3
import logging


def main():
    conn = sqlite3.connect('dbmovies.sqlite')
    conn.cursor()
    view_db =conn.execute("SELECT * FROM movie")
    db_view = view_db.fetchall()
    for preview in db_view:
        print(preview)
    conn.execute("UPDATE MOVIE SET year = 2022 WHERE name = 'Toy Story';") # Database update
    conn.commit()
    after_update = db_view
    for new_update in after_update:
        print(new_update)
    show = conn.execute("SELECT * FROM movie;")
    
    conn.execute("DELETE FROM movie WHERE movieid = 11;") # We lost our only copy of  Lawrence of Arabia, using python and SQL delete that movie from the database
    conn.commit()
    view = show.fetchall()
    
    for movies_table in view:
        print(movies_table)
        
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')    
    logging.debug("Commit to database was successful.")
    print("Welcome to the MovieDB!\n")
    view_records()

def view_records():
    conn = sqlite3.connect('dbmovies.sqlite')
    conn.cursor()
    user_input = int(input("Please enter the year to lookup: ")) # User Lookup by Year
    #create a function that asks the user for the year and displays the movies from the database that were made in that year.  note: verify the input prior to executing the SQL
    try:
     select = conn.execute(f"SELECT * FROM movie WHERE year = {user_input};")

     print(f"{'Category'}{' '}{'Title'} {' '}{'Year'} {' '}{'Length'}")
     view_movie_db = select.fetchone()
     print(f"{view_movie_db[1]}: {view_movie_db[2]}: {view_movie_db[3]}: {view_movie_db[4]}")
     # Print a message with the title of the program
    except:
        TypeError
        print("Invalid Movie Year please try again.")
        # If no movie found, print a message to the user that no movie was found.

        
   # Use a continue (y/n) to ask the the user for another year to look up until the user selects a non-y input. 
    user_continue = str(input("Would you like to continue:(y/n)"))
    for post in user_continue:
         if post == "y":
           view_records()
         else:
           user_continue == "n"
           print("Have a good day!")
        # End the program with a parting message


    








if __name__ == "__main__":
    main()