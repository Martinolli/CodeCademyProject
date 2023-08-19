# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 08:09:14 2023

@author: Joao.Bosco/ChatGpt

Function to collect data to create a Hazard description Record


"""

from hazard_class import Hazard, UndesirableEvent, SafetyEvent

from hazard_class import Outcome, Risk_Index

from get_constraints import get_hazard_statement, get_severity_choice

from get_constraints import get_likelihood_choice, get_risk_assessment

from get_constraints import get_barriers, get_mitigations


def create_hazard():
    # Define the Hazard Statement for analysis

    hazard_statement = get_hazard_statement()

    # Collect undesirable event details

    event_description = input("Please describe the undesirable event: ")

    # Choose the Likelihood for the "Undesirable Event."

    chosen_likelihood = get_likelihood_choice()

    # Collect Safety events and for Safety /Event add a Barrier Description

    safety_events = []
    while True:
        safety_events_description = input(
            "Please describe the safety events,"
            "(causes) associated with "
            "undesirable "
            "event (or done to finish): "
        )
        if safety_events_description.lower() == "done":
            break

        barriers = get_barriers()

        safety_events.append(SafetyEvent(safety_events_description, barriers))

    # Collect outcome details for each Outcome collect information about the
    # Mitigation Strategies and associater Risk Index

    outcomes = []

    while True:
        outcome_description = input(
            "Please describe an " "outcome (or 'done' to finish): "
        )
        if outcome_description.lower() == "done":
            break

        chosen_severity = get_severity_choice()

        risk_assessment = get_risk_assessment(chosen_severity[0], chosen_likelihood[0])

        risk_indexes = []
        risk_indexes.append(Risk_Index(risk_assessment[0], risk_assessment[1]))

        mitigations = get_mitigations()

        outcomes.append(
            Outcome(outcome_description, chosen_severity, mitigations, risk_indexes)
        )

    # Create the UndesirableEvent

    undesirable_event = UndesirableEvent(
        event_description, chosen_likelihood, outcomes, safety_events
    )

    # Create the Hazard
    hazard = Hazard(hazard_statement, undesirable_event)

    return hazard
