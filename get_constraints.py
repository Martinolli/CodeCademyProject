# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:58:48 2023

@author: Joao.Bosco/ChatGpt
"""
from hazard_class import Barrier, Mitigation


def get_hazard_statement():
    while True:
        hazard_statement = input("Please describe your Hazard, "
                                 "be objective and clear: ")
        if isinstance(hazard_statement, str) and len(hazard_statement) > 10:
            return hazard_statement
        else:
            print("Invalid Input. You should describe your hazard statement"
                  " (at least 10 characters)! ")


def get_severity_choice():
    severity_options = [
        "Minor",
        "Moderate",
        "Severe",
        "Critical",
        "Catastrophic",
    ]

    while True:
        print("Choose a Severity:")

        for i, option in enumerate(severity_options):
            print(f"{i + 1}.{option}")
        severity_choice = input("Enter the number of your chosen severity: ")

        if (severity_choice.isdigit()
                and 1 <= int(severity_choice) <= len(severity_options)):

            return [int(severity_choice),
                    severity_options[int(severity_choice) - 1]]

        else:
            print("Invalid choice! Please select a number from the given "
                  "options.")


def get_likelihood_choice():
    likelihood_options = [
        "Very Low",
        "Low",
        "Medium",
        "High",
        "Very High",
    ]

    while True:
        print("Choose the Undesirable Event likelihood!")

        for i, option in enumerate(likelihood_options):
            print(f"{i + 1}.{option}")
        likelihood_choice = input("Enter the number of "
                                  "your chosen likelihood: ")

        if (likelihood_choice.isdigit() and
                1 <= int(likelihood_choice) <= len(likelihood_options)):

            return [int(likelihood_choice),
                    likelihood_options[int(likelihood_choice) - 1]]

        else:
            print("Invalid choice! Please select a number from"
                  " the given options.")


def get_barriers():

    barriers = []

    while True:
        barrier_description = input("Please describe the barriers for "
                                    "your safety event "
                                    "(or 'done' to finish): ")
        if barrier_description.lower() == 'done':
            break
        barriers.append(Barrier(barrier_description))
    return barriers


def get_mitigations():

    mitigations = []

    while True:
        mitigation_description = input("Please describe the mitigation action "
                                       "for this outcome "
                                       "(or 'done' to finish): ")
        if mitigation_description.lower() == 'done':
            break
        mitigations.append(Mitigation(mitigation_description))
    return mitigations


def get_risk_assessment(severity_level, likelihood_choice):

    risk_level = severity_level * likelihood_choice

    if severity_level == 1 and likelihood_choice in [1, 2, 3]:
        risk_assessment = 'Low Impact Assessment'

    elif severity_level == 2 and likelihood_choice in [1, 2]:
        risk_assessment = 'Low Level Assessment'

    elif severity_level == 3 and likelihood_choice in [1]:
        risk_assessment = 'Low Level Assessment'

    elif severity_level == 3 and likelihood_choice in [3]:
        risk_assessment = 'High Level Assessment'

    elif severity_level == 4 and likelihood_choice in [3, 4, 5]:
        risk_assessment = 'High Level Assessment'

    elif severity_level == 5 and likelihood_choice in [3, 4, 5]:
        risk_assessment = 'High Level Assessment'

    else:
        risk_assessment = 'Medium Level Assessment'

    return [risk_level, risk_assessment]
