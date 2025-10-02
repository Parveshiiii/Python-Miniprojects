
import random
#CATEGORIZING OUTCOME INTO A LIST

one =   """ 
            ("===========")
            ("|         |")
            ("|    O    |")
            ("|         |")
            ("===========")\n  
        
        """

two =   """ 
            ("===========")
            ("|         |")
            ("| O     O |")
            ("|         |")
            ("===========")\n  
        
        """



three =   """ 
            ("===========")
            ("|    O    |")
            ("|    O    |")
            ("|    O    |")
            ("===========")\n  
        
        """

four =   """ 
            ("===========")
            ("|  O    O |")
            ("|     0   |")
            ("|  O    O |")
            ("===========")\n  
        
        """

five =   """ 
            ("===========")
            ("| O     O |")
            ("|    0    |")
            ("| O     O |")
            ("===========")\n  
        
        """

six =  """
            ("===========") 
            ("| O     O |")
            ("| O     O |")
            ("| O     O |")
            ("===========") \n      
        """

outcomes = [one, two, three, four, five, six]

print("=================================")

x = "y"

while x == "y":
    random_outcome = random.choice(outcomes)
    print(random_outcome)   # print the whole dice face at once
    
    x = input("Press y to roll again ")

