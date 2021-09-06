from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, Separator


style = style_from_dict(
    {
        Token.Separator: "#cc5454",
        Token.QuestionMark: "#673ab7 bold",
        Token.Selected: "#cc5454",  # default
        Token.Pointer: "#673ab7 bold",
        Token.Instruction: "",  # default
        Token.Answer: "#f44336 bold",
        Token.Question: "",
    }
)


def validate_len(curr):
    try:
        p_len = int(curr)
        if p_len < 12 or p_len > 50:
            return "Password length should be between 12 and 50"
        return True
    except Exception:
        return "password length should be a number"


def validate_pass(curr):
    curr = curr.strip()
    if len(curr) < 12 or len(curr) > 50:
        return "Password length should be between 12 and 50"
    return True


def validate_input(curr):
    curr = curr.strip()
    if not curr:
        return "Field is required"
    return True


login = [
    {
        "type": "input",
        "message": "Enter your username 😃 ",
        "name": "username",
        "validate": validate_input,
    },
    {
        "type": "password",
        "message": "Enter your password 🔑",
        "name": "password",
        "validate": validate_pass,
    },
]

cred = [
    {
        "type": "list",
        "message": "create new or add existing?",
        "name": "cred_type",
        "choices": ["new", "existing"],
    }
]

existing_cred = [
    {
        "type": "input",
        "message": "Enter the account name",
        "name": "app_name",
        "validate": validate_input,
    },
    {
        "type": "input",
        "message": "Enter the account username",
        "name": "login",
        "validate": validate_input,
    },
    {
        "type": "password",
        "message": "Enter the account password",
        "name": "login_pass",
        "validate": validate_input,
    },
]

new_cred = [
    {
        "type": "input",
        "message": "Enter the account name",
        "name": "app_name",
        "validate": validate_input,
    },
    {
        "type": "input",
        "message": "Enter the account username",
        "name": "login",
        "validate": validate_input,
    },
    {
        "type": "password",
        "message": "Enter the account password 🔑 (Optional)",
        "name": "login_pass",
        "validate": lambda x: True if x == "" else validate_pass(x),
    },
    {
        "type": "input",
        "message": "Prefered password length? 📏 (Optional)",
        "name": "pass_len",
        "when": lambda answers: not bool(answers["login_pass"]),
        "validate": validate_len,
        "default": "20",
    },
]

clip = [
    {
        "type": "input",
        "message": "Enter the account name",
        "name": "app_name",
        "validate": validate_input,
    }
]

delete = [
    {
        "type": "input",
        "message": "Enter the account name",
        "name": "app_name",
        "validate": validate_input,
    }
]