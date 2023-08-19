# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:50:08 2023

@author: Joao.Bosco
"""
from main_hazard import create_hazard


def hazard_function():
    # Collect hazard details
    new_hazard = ""
    with open("hazards.txt", "a") as f:
        f.write(input("Please enter the Title of your File: ") + "\n")

        new_hazard = create_hazard()

        f.write(str(new_hazard) + "\n")
    return new_hazard
