# fieldwire_interview

# How to change browser to use:
You can change the browser you use by navigating to the config.json file and changing the variable "browser"

# Automation of Signup, Create project, create task flow
Within the file test_projects_page.py, running the test test_create_new_task will successfully automate the signup, create project, and create task flow

# Bugs found
Bug #1: Account Header is not underlined even when you're on the Account tab
Steps to reproduce:
- Click on any of the top headings that’s not Account
- Click underneath David to account

Expected Result:
- Account should be underlined

Actual Result:
- People or whatever other category is underlined

Bug #2: While first name is not filled in, account create button is clickable
Steps to reproduce:
- Fill in all details for signing up for an account except for first name

Expected Result:
- Create account button is not clickable until all required fields are filled in

Actual Result:
- Create account button is clickable


