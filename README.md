# Password-Locker

## Built By [Hannah Waruguru](https://github.com/HWaruguru/)

## Description
Password Locker is a pyinquirer and docopt terminal run python application that allows users to store usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display the pyinquirer and docopt terminal | **In pyinquirer and docstring terminal: python pass_locker_cmd.py -i** | Welcome to Hpass! (type help for a list of commands.) |
| Display prompt for navigating to an option | **Enter: help** | Commands available:help -> show help message, Signup->Signup - requires username and password, login ->login - requires username and password, add_credential ->add a redential account, copy_credential ->copy a credentials username and password, show_credentials ->show all saved credentials, delete_credential ->delete a credential account  |
| Display prompt for sign up and creating credentials | **Enter: signup** | create new or add existing? - choose new, Enter the account name, Enter the account password (Optional) - enter a preffered password  or Enter to generate a password,  Prefered password length? - choose a number between 12 and 50 for a prefferd password length |
| Display a table of credentials | **Enter: show_credentials** | Prints a table of saved credentials |
| Display prompt for logging in | **Enter: login** | Enter the username and Enter your password |
| Display prompt for deleting an account | **Enter: delete_credentials** | Enter the account name to be deleted |
| Display prompt for log out | **Enter: logout** | Good Bye |


## SetUp / Installation Requirements
### Prerequisites
* python 3.9
* pip
* pyperclip
* docopt
* pyinquirer

### Cloning
* In your terminal:
        
        $ git clone https://github.com/HWaruguru/Password-Locker.git
        $ cd Password-Locker

## Running the Application
* To run the application, in your pyinquirer and docopt terminal:

        -> python pass_locker_cmd.py -i
        -> type help  to see the options available
        
## Testing the Application
* To run the tests for the class file:

        $ python user_test.py
        $ python credentials_test.py
        
## Technologies Used
* Python3.9

## License
MIT &copy;2021 [Hannah Waruguru](https://github.com/HWaruguru/)

