import pandas as pd
import matplotlib.pyplot as plt 

 
# Create class Violent Children
class Violent_Children:
    def __init__(self,dataframe):
    #    self.value = value
       self.dataframe = dataframe #Read Dataset save in cwd
      
    def dataset(self):
    #  dataframe = pd.read_csv("childrens_violence new.csv") #Read Dataset save in cwd
     input_value = str(input("Choose what discipline code you would like to know more about: ")).capitalize() #Get users value
     view_row =self.dataframe[self.dataframe["Entity"] == input_value]#Pass the user's value 
     print(view_row) #Print filtered data
     
     user_continue = input("Would you view any other records? ")
     if user_continue == str('yes'): #If condtional is met proceed to next line of code
           self.dataset() #This will call the dataset function
     elif user_continue == str('no'): #If conditional is met it breaks the loop and prints Have a good day
         print("Have a good day!")
          
 #Main program for accessing the dataset   
def main():
    print("Here are the Top 10 Violent Children by Discilpline by Code")
    df = pd.read_csv("childrens_violence new.csv")
    pd.set_option('display.max.rows',73) #found the issue with not able to print all 73, remove the .head from the code
    print(df.head(10)["Entity"])
    # print(df["Entity"])
    # df.plot()
    
    # data = Violent_Children(pd.read_csv("childrens_violence new.csv"))
    # data.dataset()
    
    
    
    

     
    
    
          
if __name__ == '__main__':
    main()

