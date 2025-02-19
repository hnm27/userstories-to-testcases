# User Stories to Test Cases

This repository is the artifact for the research paper: **"From User Stories to End-to-End Web Testing"** by
Humaid Mollah and Petra van den Bos (Formal Methods and Tools Group, University of Twente, Enschede, The Netherlands). The paper has been submitted to the ICTS workshop INTUITESTBEDS 2023.

## Repository Contents

This repository contains:

1. Source code for the test cases used in the case studies discussed in the paper.
2. Interview transcripts from discussions with software developers and testers at the digital development agency **[El Nino](https://elnino.tech/)**.

## Case Study Web Applications

1. **MyDay**: [https://app.myday.me](https://app.myday.me)
2. **VRM**: [https://vrm.victronenergy.com](https://vrm.victronenergy.com)
3. **Utwente People**: [https://people.utwente.nl/](https://people.utwente.nl/)

## Project Structure

- `/tests` - Contains test case implementations for MyDay, VRM, and Utwente People web applications.
- `/user_actions` - Contains user action implementations using the Selenium WebDriver.
- `/helper` - Contains helper functions for Selenium WebDriver operations.
- `main.py` - Entry point to run all test cases and generate reports.
- `interview_transcripts.pdf` - Contains the interview transcripts.

## Instructions to Run the Test Cases

### Prerequisites

Ensure that your system meets the following requirements:

1. **Python 3.10 or higher** is installed.
2. **Google Chrome or Mozilla Firefox** is installed.
3. **Stable Internet connection** is available.

### Setup Instructions

1. The project dependencies are managed using **Pipenv**. If Pipenv is not installed, run the following command:
   ```sh
   pip install pipenv
   ```

2. Install the required dependencies by running:
   ```sh
   pipenv sync
   ```

3. Activate the virtual environment:
   ```sh
   pipenv shell
   ```

### Configuring the WebDriver

By default, the test cases run using **Google Chrome**. If you prefer to use **Firefox**, update the `initialize_webdriver()` method in `/helper/selenium_helper.py`:

1. Comment out the line that initializes the Chrome WebDriver.
2. Uncomment the line that initializes the Firefox WebDriver.

### Running the Test Cases

To execute all test cases in the `/tests` directory, use the following command:

#### Mac/Linux:
```sh
python -m unittest discover -s tests -p '*.py'
```

#### Windows:
```sh
python -m unittest discover -s tests -p *.py
```

### Running MyDay Test Cases

By default, **5 out of 6 MyDay test cases are skipped** with the following message:

> "To run this test case, enter the email and password of your MyDay.me account in the file TODOs."

To enable these test cases:

1. **Create a MyDay account** at [https://app.myday.me](https://app.myday.me).
2. **Provide your MyDay credentials**:
   - Open `tests/test_myday.py`.
   - Locate the lines marked with `TODO` comments.
   - Enter your MyDay email and password in the respective placeholders.

After completing the setup, re-run the test cases using the `unittest` command mentioned earlier.

---

For any issues or questions, feel free to reach out!

