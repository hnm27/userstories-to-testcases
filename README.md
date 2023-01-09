# userstories-to-testcases

# Research Paper : User Stories applied for end-to-end web testing 
Humaid Mollah, Petra van den Bos (Formal Methods and Tools Group, University of Twente, Enschede, The Netherlands)

This repository contains the following:
1. Source code for case studies performed in this research
2. Interview transcripts conducted on the software developers and testers of digital development agency: El nino, Enschede, The Netherlands.

# Project Structure :

/tests -  Contains test case implementations for Myday and VRM web applications <br />
/user_actions - Contains user actions implementations with the help of Selenium web driver <br />
/helper - Contains helper fuctions created with the selenium web driver <br />
main.py - Code to run all test case implementations and to generate reports <br />
interview_transcripts.txt - Contains interview transcripts

# Instructions to run the project - 

The project dependencies lie inside the Pipfile which has been created using Python's Pipenv tool. <br />
The project can be cloned and the 'pipenv sync' command can be used to download all dependencies and setup the project. For more infor visit https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv <br />
Test case implementations can be executed directly from the test files inside tests/ or from main.py


