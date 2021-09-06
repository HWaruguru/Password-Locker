import unittest
import pyperclip
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
    def setUp(self):
        '''
            Set up method to run before each test cases.
        '''
        self.new_cred = Credential("instagram", "Hannah", "hanPass1")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.account_name, "instagram")
        self.assertEqual(self.new_cred.username, "Hannah")
        self.assertEqual(self.new_cred.password, "hanPass1")


    
if __name__ == '__main__':
    unittest.main()

