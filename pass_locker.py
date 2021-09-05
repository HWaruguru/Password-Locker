from user import User
import string
import secrets
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


  def create_cred(user, account_name, username, password=None, pass_len=20):
    '''Create new credential
  
  Args:
    user: whom we creating the credentials for.
    account_name: credential account_name.
    username: credential username.
    password: credential password.
    pass_len: preffered password length.
  '''

  if not password:
    password = generate_password(pass_len)

  cred = Credential(account_name, username, password)
  CREDS[user.username][account_name] = cred.__dict__
  return f"credential for account {account_name} created succesfully"

def generate_password(pass_len):
  '''generate a new password
  
  Args:
    pass_len: preffered password length.
  '''

  return "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(pass_len))

def delete_cred(user, account_name):
  if CREDS[user.username].get(account_name):
    CREDS[user.username].pop(account_name)
    return f"Account {account_name} deleted succesfully"
  else:
    return f"Account {account_name} does not exist"

def login(username, password):
  if not ACCOUNTS.get(username):
    return f"username {username} does not exist"
  if ACCOUNTS[username].get("password") != password:
    return "Invalid password"
  return User(username, password)

def copy(username, account_name):
  if not CREDS[username].get(account_name):
    return f"Account {account_name} does not exist"
  account = CREDS[username].get(account_name)
  pyperclip.copy(f"{account['username']} {account['password']}")


def show_creds(user):
  if not CREDS[user.username].values():
    return "You don't have any credentials saved yet!"

  headers = ["Account", "Username", "Password"]
  values = [
    [c["account_name"], c["username"], c["password"]] for c in CREDS[user.username].values()
  ]
  data = [headers]
  data.extend(values)
  return data