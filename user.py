class User:
    """
    Class that creates user accounts and saves the user's information.
    """

    def __init__(self, username, password):
        '''
          __init__ method that helps us define properties for each object.

          Args:
              username: New user object username.
              password : New user object password.
          '''

        self.username = username
        self.password = password
