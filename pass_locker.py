from user import User
from os.path import isfile
import json

def load_data():
    accs = {}
    creds = {}
    if isfile("accounts.json"):
        try:
            with open("accounts.json", "r") as acc_f:
                accs = json.load(acc_f)
        except Exception:
            pass
    if isfile("creds.json"):
        try:
            with open("creds.json", "r") as creds_f:
                creds = json.load(creds_f)
        except Exception:
            pass
    return accs, creds


ACCOUNTS, CREDS = load_data()


def persist_data():
    try:
        with open("accounts.json", "w") as outfile:
            json.dump(ACCOUNTS, outfile)
    except Exception:
        pass

    try:
        with open("creds.json", "w") as outfile:
            json.dump(CREDS, outfile)
    except Exception:
        pass

def create_user(username, password):
  '''Create new user
  
  Args:
    username: user username.
    password: user password.
  '''
  user = User(username, password)
  ACCOUNTS[user.username] = user.__dict__
  CREDS[user.username] = {}
  return user
