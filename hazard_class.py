# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 08:03:28 2023

@author: Joao.Bosco/ChatGpt

This code describes the classes used to define a "Hazard Analysis,"
It is not completed or exhaustive, but it encapsulate the following
hazard elements according to good practices:
    1 - Class Hazard:
        Hazard Id.
        Hazard Statement - a Hazard Description
        Undesirable Event.
        Date and time from Analysis.
    2 - Class Undesirable Event:
        Undesirable Event Description
        The Likelihood associated with it is qualitative value.
        Outcomes Related to the Safety Event
        Safety Events associated with Undesirable Events - Causes
    3 - Class Likelihood:
        Likelihood Level; 1 to 5
        Likelihood Description: from Very Low to High.
    4 - Class Safety Events:
        Safety Event Description - The main causes for Undesirable Event
        Safety Event ID - Identification for each Safety Event
        Barriers - The main Barriers to avoiding escalation to an Undesirable Event
    5 - Barriers:
        Barrier ID - For each barrier has one Id
        Barrier Description - Detailed description of a strategy to avoid the
        Undesirable event or to avoid escalation from Safety Event to
        Undesirable event
    6 - Outcomes:
        Outcome Description - The probable consequence after the Undesirable 
        The event is acceptable for more than one outcome, for example, assets 
        consequences, people consequences, material, environment, etc.
        Severity - For each outcome, one severity index and class.
        Mitigation - for each outcome, more than one mitigation strategy could
        be defined.
        Risks - for each outcome, one level of risk related to undesirable 
        event likelihood and outcome severity, and the risk assessment.
    7 - Severity:
        Level - according to the table below
        Description - according to the table below
    8 - Mitigation:
        Description - a type of mitigation strategy for each outcome of more than
        one mitigation is possible
        Mitigation Id - for each outcome, one Id is generated
    9 - Risk Index:
        Risk Index - is the result of "likelihood" and "severity" for each
        outcome
        Risk Assessment - the class associated with the risk index.                


Remarks:
	Horizontal Axe = Severities Levels
	Vertical Axe = Likelihood Levels
	Risk Index and Risk Assessment Levels are in the Matrix Box

	The Severity Levels and Likelihood Levels can be changed accordingly.

----------------------------------------------------------------------
-                       Minor Moderate Severe Critical Catastrophic  -
-                         1      2       3       4          5        -
----------------------------------------------------------------------
   Very High	-  5	  5     10      15      20         25        -
----------------------------------------------------------------------
     High       -  4	  4      8      12      16         20        -
----------------------------------------------------------------------
    Medium      -  3	  3      6       9      12         15        -
---------------------------------------------------------------------- 						                             -
     Low        -  2      2      4       6       8         10        -
----------------------------------------------------------------------						                             -
   Very Low	-  1	  1      2       3       4          5        -
----------------------------------------------------------------------						                             -

"""

from datetime import datetime


class Hazard:
    def __init__(self, hazard_statement, undesirable_event):
        self.hazard_id = self.generate_id()
        self.hazard_statement = hazard_statement
        self.undesirable_event = undesirable_event
        self.date_identified = datetime.now()

    # This is the routine to calculate the Hazard Ids
    def generate_id(self):
        # Read the last used Id from a file
        try:
            with open('last_id.txt', 'r') as file:
                last_id = int(file.read().strip())
        except FileNotFoundError:
            last_id = 0
        # Increment Id
        new_id = last_id + 1

        # Write the new Id back to the file
        with open('last_id.txt', 'w') as file:
            file.write(str(new_id))

        # Return the new Id in the desired format
        id_date = datetime.now().strftime('%Y%m%d')
        return f"HZ_{new_id:04d}_{id_date}"

    def __repr__(self):
        return (f"Hazard ID: {self.hazard_id}\n"
                f"Hazard Statement: {self.hazard_statement}\n"
                f"Undesirable Event: {self.undesirable_event}\n"
                f"Date Identified: {self.date_identified}\n")


"""This part of code define the "construction", "attributes," and
"methods" for UndesirableEvent - Description, Likelihood,
Outcomes and Safety Events (causes) associated with."""


class UndesirableEvent:
    def __init__(self, description, likelihood, outcomes, safety_events):
        self.description = description
        self.likelihood = likelihood            # Instance of likelihood
        self.outcomes = outcomes                # List of Outcome instances
        self.safety_events = safety_events      # List of SafetyEvent instances

    def __repr__(self):
        outcomes = "\n".join(str(outcome) for outcome in self.outcomes)
        safety_events = "\n".join(str(safetyevent)
                                  for safetyevent in self.safety_events)
        return (f"Event Description: {self.description}\n"
                f"Likelihood: {self.likelihood}\n"
                f"Outcomes: {outcomes}\n"
                f"Safety Events: {safety_events}\n")


class Likelihood:
    def __init__(self, level, description):
        self.level = level
        self.description = description

    def __repr__(self):
        return (f"Likelihood Level: {self.level}\n"
                f"Likelihood Description: {self.description}\n")


"""This part of code define the "construction", "attributes,"
 and "methods" for Safety Events, Barriers."""


class SafetyEvent:
    def __init__(self, description, barriers):
        self.safety_event_id = self.generate_safety_event_id()
        self.description = description
        self.barriers = barriers      # This would be an instance of Barrier

    # This is the routine to calculate the Safety Event Ids
    def generate_safety_event_id(self):
        # Read the last used Id from a file
        try:
            with open('safety_event_last_id.txt', 'r') as file:
                last_id = int(file.read().strip())
        except FileNotFoundError:
            last_id = 0
        # Increment Id
        new_id = last_id + 1

        # Write the new Id back to the file
        with open('safety_event_last_id.txt', 'w') as file:
            file.write(str(new_id))

        # Return the new Id in the desired format
        return f"SE_{new_id:04d}"

    def __repr__(self):
        barriers = "\n".join(str(barrier) for barrier in self.barriers)
        return (f"Safety Event ID: {self.safety_event_id}\n"
                f"Safety Event Description: {self.description}\n"
                f"Safety Barriers: {barriers}\n")


class Barrier:
    def __init__(self, description):
        self.description = description
        self.barrier_id = self.generate_barrier_id()

        # This is the routine to calculate the Barriers Ids

    def generate_barrier_id(self):

        # Read the last used Id from a file
        try:
            with open('barrier_last_id.txt', 'r') as file:
                last_id = int(file.read().strip())
        except FileNotFoundError:
            last_id = 0
        # Increment Id
        new_id = last_id + 1

        # Write the new Id back to the file
        with open('barrier_last_id.txt', 'w') as file:
            file.write(str(new_id))

        # Return the new Id in the desired format
        return f"BR_{new_id:04d}"

    def __repr__(self):
        return (f"Barrier ID: {self.barrier_id}\n"
                f"Barrier Description: {self.description}\n")


"""This part of code define the "construction", "attributes," and "methods"
specific for Outcome, Severity, and Mitigation."""


class Outcome:
    def __init__(self, description, severity, mitigations, risks):
        self.description = description
        self.severity = severity        # Instance of Severity
        self.mitigations = mitigations  # Instance of Mitigation
        self.risks = risks    # Instance of Risk Index

    def __repr__(self):

        mitigations = "\n".join(str(mitigation)
                                for mitigation in self.mitigations)
        risks = "\n".join(str(risk_index) for risk_index in self.risks)
        return (f"Outcome Description: {self.description}\n"
                f"Outcome Severity: {self.severity}\n"
                f"Outcome Mitigation:,{mitigations}\n"
                f"Risk Level: {risks}\n")


class Severity:
    def __init__(self, level, description):
        self.level = level
        self.description = description

    def __repr__(self):
        return (f"Severity Level: {self.level}\n"
                f"Severity Description: {self.description}\n")


class Mitigation:
    def __init__(self, description):
        self.description = description
        self.mitigation_id = self.generate_mitigation_id()

    def generate_mitigation_id(self):
        """This is the routine to calculate the Mitigation Ids
        """
        # Read the last used Id from a file
        try:
            with open('mitigation_last_id.txt', 'r') as file:
                last_id = int(file.read().strip())
        except FileNotFoundError:
            last_id = 0

        # Increment Id

        new_id = last_id + 1

        # Write the new Id back to the file

        with open('mitigation_last_id.txt', 'w') as file:
            file.write(str(new_id))

        # Return the new Id in the desired format

        return f"MT_{new_id:04d}"

    def __repr__(self):
        return (f"Mitigation ID: {self.mitigation_id}\n"
                f"Mitigation Description: {self.description}\n")


class Risk_Index:
    def __init__(self, risk_index, risk_assessment):
        self.risk_index = risk_index
        self.risk_assessment = risk_assessment

    def __repr__(self):
        return (f"Risk Index: {self.risk_index}\n"
                f"Risk Assessment: {self.risk_assessment}\n")
