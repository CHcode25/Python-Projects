import pandas as pd
import matplotlib.pyplot as plt 

 
# Create class Violent Children
class Violent_Children:
    def __init__(self,year):
        self.year = year
   
      
    def dataset(self):
        dataset = pd.read_csv("childrens_violence new.csv")
        
        display = dataset.loc[self.year] #Taking user input by row number
        print(display) #Print filtered data
     
      
          
#Print the 
def main():
     df = pd.read_csv("childrens_violence new.csv")
     pd.options.display.max_rows = 10
     print("Here are the Top 10 Violent Children by Discilpline by Code")
     print(df)
     records()
 
#Main program for accessing the dataset    
def records():
     user_data =int((input("Enter a rows 0-72 to view records: ")))
     rec = Violent_Children(user_data)
     rec.dataset()
     
     user_continue = input("Would you view any other records? ")
     if user_continue == str('yes'): #If condtional is met proceed to next line of code
         records()
            #This will call the dataset function
     elif user_continue == str('no'): #If conditional is met it breaks the loop and prints Have a good day
         print("Have a good day!")
     
    
   
if __name__ == '__main__':
    main()

