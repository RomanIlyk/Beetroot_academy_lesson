#Write tests for the Phonebook application, which you have implemented in module 1.
# Design tests for this solution and write tests using unittest library
import json
import unittest
from unittest.mock import patch
import book_methods
data_ph = open("data_phonebook.json","r+")
data = json.load(data_ph)

class TestPhonebookMethods(unittest.TestCase):
    #Test add function
    @patch('builtins.input', side_effect=('+30956380996', 'Yra', 'Koss','Kyiv'))
    def test_add(self,mock_input):
        test_add_data = book_methods.add(data,number = mock_input, first_name = mock_input,
                                         last_name = mock_input,city = mock_input)
        self.setUp()
        self.assertEqual(type([test_add_data]),type([data]))

    #Test read function
    def test_type_read_book(self):
        self.assertEqual(type([book_methods.read(data)]),list)


unittest.main()