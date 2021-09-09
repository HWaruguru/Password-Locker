"""
Hpass app cmd interface

Usage:
    my_program login
    my_program signup
    my_program (-i | --interactive)
    my_program (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from PyInquirer import prompt as get_ans
from terminaltables import SingleTable

from pass_locker import (
    create_user,
    persist_data,
    create_cred,
    delete_cred,
    copy as clip_cred,
    show_creds,
    login as _login,
)
from prompt import login, style, cred, existing_cred, new_cred, clip, delete


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print("Invalid Command!")
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class HpassInteractive(cmd.Cmd):
    intro = "Welcome to Hpass!" + " (type help for a list of commands.)"
    prompt = "Hpass: -> "
    user = None

    @docopt_cmd
    def do_signup(self, arg):
        """Usage: signup """
        if not self.user:
            _user = get_ans(login, style=style)
            self.prompt = f"Hpass: ({_user.get('username')}) -> "
            self.user = create_user(_user["username"], _user["password"])
        else:
            print(f"{self.user.username}, you are already logged in!")

    @docopt_cmd
    def do_login(self, arg):
        """Usage: signup """
        if not self.user:
            _params = get_ans(login, style=style)
            _user = _login(_params["username"], _params["password"])
            if isinstance(_user, str):
                print(_user)
            else:
                self.user = _user
                self.prompt = f"Hpass: ({self.user.username})-> "
        else:
            print(f"{self.user.username}, you are already logged in!")

    @docopt_cmd
    def do_add_credential(self, arg):
        """Usage: add_credential """
        if not self.user:
            print(":Denied! You must be logged in, please login")
        else:
            _cred = get_ans(cred, style=style)
            if _cred["cred_type"] == "new":
                _params = get_ans(new_cred, style=style)
            else:
                _params = get_ans(existing_cred, style=style)

            app_name = _params.get("app_name")
            login = _params.get("login")
            login_pass = _params.get("login_pass")
            pass_len = int(_params.get("pass_len")) if _params.get("pass_len") else 20

            print(create_cred(self.user, app_name, login, login_pass, pass_len))

    @docopt_cmd
    def do_copy_credential(self, arg):
        """Usage: copy_credential """
        if not self.user:
            print(":Denied! You must be logged in, please login")
        else:
            _params = get_ans(clip, style=style)
            app_name = _params.get("app_name")
            clip_cred(self.user.username, app_name)
            print(f"{app_name} credentials copied to clipboard")

    @docopt_cmd
    def do_show_credentials(self, arg):
        """Usage: show_credential """
        if not self.user:
            print(":Denied! You must be logged in, please login")
        else:
            data = show_creds(self.user)
            if isinstance(data, str):
                print(data)
            else:
                table = SingleTable(data)
                print(table.table)

    @docopt_cmd
    def do_delete_credential(self, arg):
        """Usage: delete_credential """
        if not self.user:
            print(":Denied! You must be logged in, please login")
        else:
            _params = get_ans(delete, style=style)
            app_name = _params["app_name"]
            print(delete_cred(self.user, app_name))

    def do_help(self, arg):
        print(
            """
        \t Commands available:
        \t help -> \t show help message \n
        \t signup  -> \t signup - requires username and password\n
        \t login -> \t login - requires username and password \n
        \t add_credential -> \t add a redential account \n
        \t copy_credential -> \t copy a credentials username and password \n
        \t show_credentials -> \t show all saved credentials \n
        \t delete_credential -> \t delete a credential account \n
        \t logout -> \t quits the commandline \n
        """
        )

    def do_logout(self, arg):
        """Logs out a user"""
        persist_data()
        print("Good Bye!")
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt["--interactive"]:
    HpassInteractive().cmdloop()

print(opt)