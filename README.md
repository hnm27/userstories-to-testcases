# userstories-to-testcases

This repository is the artefact for the research paper: "From User Stories to End-to-end Web Testing" by
Humaid Mollah and Petra van den Bos (Formal Methods and Tools Group, University of Twente, Enschede, The Netherlands).
The paper has been submitted at ICTS workshop INTUITESTBEDS 2023.

This repository contains the following:

1. Source code for the test cases of the case studies of the paper
2. Interview transcripts of the interviews with the software developers and testers of the digital development agency El nino

# Case study web applications

1. MyDay: https://app.myday.me
2. VRM: https://vrm.victronenergy.com
3. Utwente People: https://people.utwente.nl/

# Project Structure

`/tests` - Contains test case implementations for Myday, VRM, and Utwente People web applications <br />
`/user_actions` - Contains user actions implementations with the help of Selenium web driver <br />
`/helper` - Contains helper fuctions created with the selenium web driver <br />
`main.py` - Code to run all test case implementations and to generate reports <br />
`interview_transcripts.pdf` - Contains the interview transcripts

# Instructions to run the test cases 

0. We assume that your system has:<br/>
	a. python 3.10 (or a higher version) installed,<br/>
	b. browser Chrome or Firefox installed, and<br/>
	c. a connection to the Internet.

1. The project dependencies lie inside the `Pipfile`. It uses Python's Pipenv tool to install dependencies. 
If you don't have Pipenv installed on your device, run the following command on your terminal: `pip install pipenv`

2. To install the project dependencies, use the following commands:<br/>
	a. `pipenv sync` (to download all dependencies from the Pipfile)<br/>
	b. `pipenv shell` (to create a new virtual environment and activate it)

3. By default, the Chrome browser is used to execute the tests. If you want to use Firefox instead, you change the used webdriver in method `initialize_webdriver()` of file `/helpers/selenium_helper.py`:<br/>
	a. Comment out the return statement to use the Chrome webdriver<br/>
	b. Remove comment in front of the return statement to use the Firefox webdriver


4. To run all tests in the /tests directory, run the following command in a terminal:<br/>
	a. Mac/Linux: `python -m unittest discover -s tests -p '*.py'`<br/>
	b. Windows: `python -m unittest discover -s tests -p *.py`

5. Note: by default 5 out of 6 test cases of MyDay are skipped, with the following message: "To run this test case, enter the email and password of your Myday.me account in the file TODOs". To execute these test cases, you need to insert the email and password test inputs in the test cases. Do this as follows:<br/>
	a. Create an account at the MyDay website.<br/>
	b. Enter the email and password of your MyDay account in the file `tests/test_myday.py` at the 2 lines with a `TODO` comment.



