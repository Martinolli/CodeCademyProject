# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:50:08 2023

@author: Joao.Bosco
"""
from main_hazard import create_hazard


# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:50:08 2023

@author: Joao.Bosco
"""
from main_hazard import create_hazard

def hazard_function():
    try:
        print("Starting hazard function...")
        # Collect hazard details
        new_hazard = ""
        with open("hazards.txt", "a") as f:
            title = input("Please enter the Title of your file: ")
            f.write(title + "\n")
            print(f"Title '{title}' written to file!\n")
        
            new_hazard = create_hazard()
            f.write(str(new_hazard) + "\n")
            print(f"Hazard '{new_hazard}' written to file!\n")
                    
        print("Hazard details written to file successfully!")
        return new_hazard
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to test
hazard_function()
            