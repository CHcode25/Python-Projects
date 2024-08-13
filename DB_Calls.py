import sqlite3
import logging


def main_program():
    db_connection = sqlite3.connect('Movies.sqlite')
    db_connection.cursor()
    movies_infor_2 = "UPDATE movies_info_2 SET release_year='2006', description= 'DC Comics' WHERE show_id=4;"
    
    db_connection.execute(movies_infor_2)
    db_connection.commit()
    response = db_connection.execute("SELECT * FROM movies_info_2;")
    retrieve_results = response.fetchall()
    
    #Using for loop to print results as a tuple
    for view_data in retrieve_results:
        print(view_data)
    
    #Closing database connection 
    db_connection.close()
    
#Setting logging paramters 
logging.basicConfig(level=logging.INFO,filename="logs.txt")
logging.debug(True)  

if __name__ == '__main__': 
    main_program()