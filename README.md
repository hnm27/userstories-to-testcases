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

[ Note : the testfile test_myday.py contains 2 TODOS which are test inputs required to run the test cases in this test class. If these are not completed 5/6 test cases will fail with the following error: "AssertionError: To run this test case, enter the email and password of your Myday.me account in the file TODOs" ] 

The project dependencies lie inside the Pipfile which has been created using Python's Pipenv tool. <br />

If you don't have Pipenv install, run the following command on your termnal: 
pip install pipenv

To install the project dependencies use the following commands:
1. pipenv sync (to download all dependencies in the Pipfile)
2. pipenv shell (to create a new virtual environment and activate it)

To run all tests in the /tests directory, run the following command:
python -m unittest discover -s tests -p '*.py'




