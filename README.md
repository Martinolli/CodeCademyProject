# CodeCademyProject
## Portfolio Project Codecademy Course
**Hazard Analysis Tool**
This piece of code is composed of the following codes:
- call_hazard.py
- main_hazard.py
- get_constraints.py
- hazard_class.py
### Remarks
This piece of code is not exhaustive is a primary idea to generate a code to perform a hazard analysis qualitatively based on 
the "bowtie" analysis.
The idea is to develop a simple prototype for a more complex tool to perform risk analysis.


### call_hazard.py
It is a function used to interact with the main_hazard code and initialize the collection of information about a "hazard analysis."
This function collects and stores the data in a "txt" file.

### main_hazard.py
It is a function used to interact with the other two codes, "get_constraints" and hazard_class.
This function calls the other two functions and defines some figures necessary to perform the analysis.

### get_constraints.py
It is a collection of small pieces or functions to perform tasks necessary to store data.

### hazard_class.py
In this file are defined all class for hazard analysis.
- Hazard id
- Hazard statement
- Undesirable Event
- Safety Events - Causes
- Barriers
- Outcomes
- Mitigations
- Likelihood - Associated with undesirable event
- Severity - Associated with Outcomes
- Risk - Associated with each outcome

