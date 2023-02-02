# userstories-to-testcases

This repository is the artefact for the research paper: "From User Stories to End-to-end Web Testing" by
Humaid Mollah and Petra van den Bos (Formal Methods and Tools Group, University of Twente, Enschede, The Netherlands).
The paper has been submitted at ICTS workshop INTUITESTBEDS 2023.

This repository contains the following:
1. Source code for case studies performed in this research
2. Interview transcripts from the interviews held with the software developers and testers of the digital development agency: El nino, Enschede, The Netherlands.

# Case study web applications
MyDay: https://app.myday.me<br />
VRM: https://vrm.victronenergy.com<br />
Utwente People: https://people.utwente.nl/

# Project Structure

/tests -  Contains test case implementations for Myday, VRM, and Utwente People web applications <br />
/user_actions - Contains user actions implementations with the help of Selenium web driver <br />
/helper - Contains helper fuctions created with the selenium web driver <br />
main.py - Code to run all test case implementations and to generate reports <br />
interview_transcripts.pdf - Contains interview transcripts

# Instructions to run the project 

The project dependencies lie inside the Pipfile which has been created using Python's Pipenv tool. <br />
If you don't have Pipenv install on your device, run the following command on your termnal: 
pip install pipenv

To install the project dependencies, use the following commands:
1. pipenv sync (to download all dependencies from the Pipfile)
2. pipenv shell (to create a new virtual environment and activate it)

To run all tests in the /tests directory, <br/>

1. Select the correct webdriver: <br/>
In /helpers/selenium_helper.py, choose the correct selenium web driver in the initialize_webdriver() method, either Chrome or Firefox. By default, we use the Chrome webdriver, however, if we want to use the Firefox webdriver, we can comment out the command to initialize the Chrome webdriver and uncomment the Firefox webdriver to make the transition.


2. Run the following command:<br />
For Mac terminal - python -m unittest discover -s tests -p '*.py'<br />
For Windows command line - python -m unittest discover -s tests -p *.py

[ Note : the testfile test_myday.py contains 2 TODOS which are test inputs required to run the test cases in this test class. If these are not completed 5/6 test cases will be skipped with the following message: To run this test case, enter the email and password of your Myday.me account in the file TODOs" ]



