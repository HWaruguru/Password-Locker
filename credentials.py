class Credential:
    """
      Class that creates account credentials, generates passwords and saves the information.
      """
    def __init__(self, account_name, username, password):
        '''
          __init__ method that helps us define properties for each object.

          Args:
              account_name: Name of the account.
              username: New credential object username.
              password : New credential object password.
          '''
        self.account_name = account_name
        self.username = username
        self.password = password
 